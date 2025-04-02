from textnode import *
import enum
import textwrap
import htmlnode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        # handle non-NORMAL_TEXT nodes first
        if node.text_type != TextType.NORMAL_TEXT:
            processed_children = split_nodes_delimiter([TextNode(node.text, TextType.NORMAL_TEXT, node.url)], delimiter, text_type)
            for child in processed_children:
                new_list.append(TextNode(child.text, node.text_type, node.url))
        else:
            # split text into temp_list using the delimiter
            temp_list = node.text.split(f"{delimiter}")

            # Ensure delimiters are matched
            if len(temp_list) % 2 == 0:
                raise Exception(f"Unmatched delimiter: '{delimiter}' in node text '{node.text}'")
            
            # Process each chunk in temp_list
            for index, item in enumerate(temp_list):
                if index % 2 == 0:    # Even index => normal text
                    new_list.append(TextNode(item, TextType.NORMAL_TEXT))
                elif index % 2 == 1:  # Odd index => special text type
                    new_list.append(TextNode(item, text_type))
        
    return new_list

def extract_markdown_images(text):
    # takes raw markdown and returns list of tuples
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    #each tuple should contain alt text and URL of any markdown images

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    # should behave similar to split_nodes_delimiter, but for images
    new_list = []
    for node in old_nodes:
    # For non-NORMAL_TEXT nodes, add them directly
        if node.text_type != TextType.NORMAL_TEXT:
            new_list.append(node)
        else:
            #Extract markdown images, if any
            image_tuples = extract_markdown_images(node.text)
            if not image_tuples:
                # if no images found, add node as-is
                new_list.append(node)
            else:
                remaining_text = node.text
                # iterate over extracted images to split the text
                for alt_text, url in image_tuples:
                    sections = remaining_text.split(f"![{alt_text}]({url})", 1)

                    # add text before the image (if not empty)
                    if sections[0] != "":
                        new_list.append(TextNode(sections[0], TextType.NORMAL_TEXT))
                    #add image node
                    new_list.append(TextNode(alt_text, TextType.IMAGE, url))
                    #update remaining text
                    remaining_text = sections[1]
                #add remaining text if not empty
                if remaining_text != "":
                    new_list.append(TextNode(remaining_text, TextType.NORMAL_TEXT))
    return new_list

            




def split_nodes_link(old_nodes):
        # should behave similar to split_nodes_delimiter, but for links
    new_list = []
    for node in old_nodes:
    # For non-NORMAL_TEXT nodes, add them directly
        if node.text_type != TextType.NORMAL_TEXT:
            new_list.append(node)
        else:
            #Extract markdown links, if any
            link_tuples = extract_markdown_links(node.text)
            if not link_tuples:
                # if no links found, add node as-is
                new_list.append(node)
            else:
                remaining_text = node.text
                # iterate over extracted links to split the text
                for anchor_text, url in link_tuples:
                    sections = remaining_text.split(f"[{anchor_text}]({url})", 1)

                    # add text before the link (if not empty)
                    if sections[0] != "":
                        new_list.append(TextNode(sections[0], TextType.NORMAL_TEXT))
                    #add image node
                    new_list.append(TextNode(anchor_text, TextType.LINK, url))
                    #update remaining text
                    remaining_text = sections[1]
                #add remaining text if not empty
                if remaining_text != "":
                    new_list.append(TextNode(remaining_text, TextType.NORMAL_TEXT))
    return new_list

def text_to_textnodes(text):
    initial_node = [TextNode(text, TextType.NORMAL_TEXT)]
    first_images = split_nodes_image(initial_node)
    second_links = split_nodes_link(first_images)
    now_bold = split_nodes_delimiter(second_links, "**", TextType.BOLD)
    and_italics = split_nodes_delimiter(now_bold, "_", TextType.ITALIC_TEXT)
    then_code = split_nodes_delimiter(and_italics, "`", TextType.CODE_TEXT)
    return then_code

def markdown_to_blocks(markdown):
    markdown = textwrap.dedent(markdown)
    new_list = markdown.split("\n\n")
    keep_list = []
    for block in new_list:
        stripped_block = block.strip()
        if stripped_block:
            keep_list.append(stripped_block)
    return keep_list

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if (
        block[0] == "#" or 
        block[:2] == "##" or
        block[:3] == "###" or
        block[:4] == "####" or
        block[:5] == "#####" or
        block[:6] == "######"
        ):
        return BlockType.HEADING
    elif (
        block[:3] == "```" and
        block[-3:] == "```"
        ):
        return BlockType.CODE
    lines = block.split("\n")
    quote_condition = all(line.startswith(">") for line in lines)
    if quote_condition:
        return BlockType.QUOTE
    unordered_list_condition = all(line.startswith("- ") for line in lines)
    if unordered_list_condition:
        return BlockType.UNORDERED_LIST
    ordered_list_condition = all(line.startswith(f"{index + 1}. ") for index, line in enumerate(lines))
    if ordered_list_condition:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH