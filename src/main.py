from textnode import *

def main():
    test = TextNode("this is my anchor", TextType.LINK, "https:www.treever.com")
    print(test)


if __name__ == "__main__":
    main()