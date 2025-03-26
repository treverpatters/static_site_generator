import unittest

from htmlnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "The text inside the paragraph", ["list", "listthings"], {"this": "is", "a": "dictionary"})
        node2 = HTMLNode("h1", "The text inside the paragraph", ["list", "listthings"], {"this": "is", "a": "dictionary"})
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = HTMLNode(None, "The text inside the paragraph", ["list", "listthings"], {"this": "is", "a": "dictionary"})
        node2 = HTMLNode("h1", "The text inside the paragraph", ["list", "listthings"], {"this": "is", "a": "dictionary"})
        self.assertNotEqual(node, node2)
    def test_different_types(self):
        node = HTMLNode(None, "The text inside the paragraph", ["list", "listthings"], {"this": "is", "a": "dictionary"})
        node2 = HTMLNode("h1", "The text inside the paragraph", ["list", "listthings"], {"this": "is", "a": "dictionary"})
        self.assertNotEqual(node, node2)
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_with_node(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    def test_with_node_again(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    


if __name__ == "__main__":
    unittest.main()