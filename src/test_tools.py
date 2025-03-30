import unittest
from tools import split_nodes_delimiter, TextNode, TextType, split_nodes_image, split_nodes_link

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
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL_TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL_TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )