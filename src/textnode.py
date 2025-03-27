from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "Normal Text"
    # **Bold Text**
    BOLD = "Bold Text"
    # _Italic text_
    ITALIC_TEXT = "Italic Text"
    # `Code text`
    CODE_TEXT = "Code Text"
    # Links, in this format: [anchor text](url)
    LINK = "link"
    # Images, in this format: ![alt text](url)
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None, alt=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
        self.alt = alt

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return ( self.text == other.text and 
                    self.text_type == other.text_type and 
                    self.url == other.url )

    def __repr__(self):
        return f"TextNode('{self.text}', {self.text_type.value}, '{self.url}')"    
          

