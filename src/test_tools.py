import unittest
from tools import split_nodes_delimiter, TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def setUp(self):
        self.single_text_node = TextNode("This is **bold** text", TextType.NORMAL_TEXT)
        self.no_delimiter_text_node = TextNode("This has no delimiter", TextType.NORMAL_TEXT)
        self.multiple_delimiters_node = TextNode("This has _italic_ and **bold**", TextType.NORMAL_TEXT)
    
    def test_basic_delimiter(self):
        old_nodes = [self.single_text_node]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        #Expected nodes after splitting
        expected = [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL_TEXT)
        ]
        self.assertEqual(new_nodes, expected)