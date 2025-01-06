


class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, htmlnode):
        if (self.tag == htmlnode.tag) and (self.value == htmlnode.value) and (self.children == htmlnode.children) and (self.props == htmlnode.props):
            return True
       
    def to_html(self):
        raise Exception("NotImplementedError")

    def props_to_html(self):
        if self.props == None:
            return ""
        return " " + " ".join(list(map(lambda x: x + "=" + '"' + self.props[x] + '"', self.props)))


class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = "", props = None):
        super().__init__(tag, value, None, props)



    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        

        

class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        super().__init__(tag, None, children)

    def to_html(self):
        if self.tag == None:
            raise ValueError("no tag")
        if self.children == None or len(self.children) == 0:
            raise ValueError("no children")
        
        return f"<{self.tag}{self.props_to_html()}>{''.join(map(lambda x:  x.to_html(), self.children))}</{self.tag}>"
