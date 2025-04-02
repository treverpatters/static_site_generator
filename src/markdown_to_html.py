from tools import *
from htmlnode import *

    # Order of operations:
    # 1. Split the markdown into blocks (already have this function)
    # 2. Loop over each block:
        # 1. Determine the type of block (already have this function)
        # 2. Based on the type of block, create a new HTMLNode with the proper data
        # 3. Assign the proper child HTMLNode objects to the block node. I created a shared `text_to_children(text)`function
        #     that works with all block types. It takes a string of text and returns a list of HTMLNodes that represent the
        #     inline markdown using previously created functions (think TextNode -> HTMLNode)
        # 4. The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. I
        #     didn't use my `text_to_children` function for this block type, I manually made a TextNode and used `text_node_to_html_node`
    # 3. Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.
    # 4. Create unit tests. 2 are given.

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children_list = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            heading_level = count_heading_level(block)
            html_block = HTMLNode(f"h{heading_level}", "", [])
        elif block_type == BlockType.CODE:
            # manually make TextNode and use text_node_to_html_node
            code_content = extract_code_content(block)
            code__text_node = TextNode(code_content, TextType.CODE_TEXT)
            code_html_node = text_node_to_html_node(code__text_node)
            pre_node = HTMLNode("pre", "", [code_html_node])
            children_list.append(pre_node)
        elif block_type == BlockType.UNORDERED_LIST or block_type == BlockType.ORDERED_LIST:
            #need each line to have <li> tag
            pass
        else:
            # Assign child HTMLNdode objects to the block node using `text_to_children(text)`
            html_block.children = text_to_children(block)
            children_list.append(html_block)
    parent_node = HTMLNode("div", "", children_list)    

    return parent_node

def assign_tag(block_type):
    # paragraph = "paragraph"
    if block_type == BlockType.PARAGRAPH:
        return "p"
    #heading still needs to be seperated based on how many # there are
    elif block_type == BlockType.HEADING:
        return ""
    #code = "code"
    elif block_type == BlockType.CODE:
        return "pre'code'"
    #quote = "quote"
    elif block_type == BlockType.QUOTE:
        return "blockquote"
    #unordered_list = "unordered list"
    elif block_type == BlockType.UNORDERED_LIST:
        return "ul"
    #ordered_list = "ordered_list"
    elif block_type == BlockType.ORDERED_LIST:
        return "ol"
    else:
        raise ValueError("no block type")

def count_heading_level(line):
    # Counts number of '#' characters at beginning of a string, ignoring white space.
    stripped_line = line.lstrip()
    if stripped_line.startswith('#'):
        count = 0
        for char in stripped_line:
            if char == '#':
                count += 1
            else:
                break
        return count
    else:
        raise ValueError("not a heading")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children

def extract_code_content(block):
    return block.strip("```")

