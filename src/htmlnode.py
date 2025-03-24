
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
            raise ValueError("no node")
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
            

            


        
    