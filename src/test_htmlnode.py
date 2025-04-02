import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
