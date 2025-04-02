from enum import Enum

def test():
    print("import test")

class TextType(Enum):
    bold_text = "bold text"
    italic_text = "italic text"
    code_text = "code text"
    link_text = "link text"
    image_text = "image text"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, textnode):
        return (self.text == textnode.text
                and self.text_type == textnode.text_type
                and self.url == textnode.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
