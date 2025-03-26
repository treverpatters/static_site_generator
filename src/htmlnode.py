
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return ( self.tag == other.tag and 
                    self.value == other.value and 
                    self.children == other.children and
                    self.props == other.props )
        
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        full_string = ""
        if self.props == None:
            return full_string
        for items in self.props:
            full_string = full_string + f' {items}="{self.props[items]}"'
        
        return full_string

    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("that's major depression")
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        full_string = ""
        if self.tag == None:
            raise ValueError("no tag")
        if self.children == None:
            raise ValueError("childless")
        
        string_to_add = f"<{self.tag}>"
        full_string += string_to_add

        for child in self.children:
            full_string += child.to_html()
        
        full_string += f"</{self.tag}>"
        return full_string
    
    def text_node_to_html_node(text_node):
        if text_node.TextType.TEXT:
            pass
        if text_node.TextType.BOLD:
            pass
        if text_node.TextType.ITALIC:
            pass
        if text_node.TextType.CODE:
            pass
        if text_node.TextType.LINK:
            pass
        if text_node.TextType.IMAGE:
            pass
            


                    

            


        
    