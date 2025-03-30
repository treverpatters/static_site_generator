from textnode import *
import htmlnode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        # handle non-NORMAL_TEXT nodes first
        if node.text_type != TextType.NORMAL_TEXT:
            new_list.append(node)
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
    #first, ensure node is an image
        if node.text_type != TextType.NORMAL_TEXT:
            new_list.append(node)
        #if yes, use extract_markdown_images
        else:
            image_tuples = extract_markdown_images(node.text)
            if not image_tuples:
                new_list.append(node)
            else:
                remaining_text = node.text
                for alt_text, url in image_tuples:
                    sections = remaining_text.split(f"![{alt_text}]({url})", 1)

                    if sections[0] != "":
                        new_list.append(TextNode(sections[0], TextType.NORMAL_TEXT))
                    new_list.append(TextNode(alt_text, TextType.IMAGE, url))
                    remaining_text = sections[1]
                if remaining_text != "":
                    new_list.append(TextNode(remaining_text, TextType.NORMAL_TEXT))
    return new_list

            




def split_nodes_link(old_nodes):
    # should behave similar to split_nodes_delimiter, but for links
    pass
