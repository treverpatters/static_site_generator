import unittest

from textnode import TextNode, TextType
from htmlnode import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("this is a text node", TextType.NORMAL_TEXT)
        node2 = TextNode("TThis is a text node", TextType.NORMAL_TEXT)
        self.assertNotEqual(node, node2)

    def test_different_types(self):
        node = TextNode("", TextType.NORMAL_TEXT)
        node2 = TextNode("", TextType.NORMAL_TEXT, "ww.")
        self.assertNotEqual(node, node2)
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, {"href": "http://example.com"})
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_link(self):
        node = TextNode("Click here", TextType.LINK, url="https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props["href"], "https://example.com")
    def test_image(self):
        node = TextNode("", TextType.IMAGE, url="https://example.com/image.jpg", alt="Example Image")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "https://example.com/image.jpg")
        self.assertEqual(html_node.props["alt"], "Example Image")
        


if __name__ == "__main__":
    unittest.main()