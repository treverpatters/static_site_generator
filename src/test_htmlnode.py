import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "The text inside the paragraph", ["list", "listthings"], {"this": "is", "a": "dictionary"})
        node2 = HTMLNode("h1", "The text inside the paragraph", ["list", "listthings"], {"this": "is", "a": "dictionary"})
        print(node.props_to_html())
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()