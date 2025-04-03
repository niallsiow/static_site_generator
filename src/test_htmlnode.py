import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode("div", "some content")
        self.assertEqual("div", node.tag)
        self.assertEqual("some content", node.value)
        self.assertEqual(None, node.children)
        self.assertEqual(None, node.props)

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "www.example.com", "target": "_blank"}) 
        self.assertEqual(' href="www.example.com" target="_blank"', node.props_to_html())

    def test_repr(self):
        node = HTMLNode("p", "some text", None, {"class": "primary"})
        self.assertEqual("HTMLNode(p, some text, children: None, {'class': 'primary'})", node.__repr__())


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello world!")
        self.assertEqual("<p>Hello world!</p>", node.to_html())

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello world!")
        self.assertEqual("Hello world!", node.to_html())

    def test_repr(self):
        node = LeafNode("p", "some text", {"class": "primary"})
        self.assertEqual("LeafNode(p, some text, {'class': 'primary'})", node.__repr__())


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual("<div><span>child</span></div>", parent_node.to_html())

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual("<div><span><b>grandchild</b></span></div>", parent_node.to_html())

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ])
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())


if __name__ == "__main__":
    unittest.main()
