from textnode import *
from tools import *

def main():
    test = TextNode("this is my anchor", TextType.LINK, "https:www.treever.com")
    print(test)
    ordered_list_block = "1. First item\n2. Second item\n3. Third item"
    print(block_to_block_type(ordered_list_block))


if __name__ == "__main__":
    main()