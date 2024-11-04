import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("Hi", TextType.ITALIC, None)
        node2 = TextNode("Hi", TextType.ITALIC, None)
        self.assertEqual(node, node2)
    
    def test_eq_3(self):
        node = TextNode("Hello", TextType.CODE, "https://www.boot.dev")
        node2 = TextNode("Hello", TextType.CODE, "https://www.boot.dev")
        self.assertEqual(node, node2)
'''
    def test_eq_4(self):
        node = TextNode("Hello", TextType.CODE, "https://www.boot.dev")
        node2 = TextNode("Hi", TextType.CODE, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_eq_5(self):
        node = TextNode("Hello", TextType.CODE, "https://www.boot.dev")
        node2 = TextNode("Hello", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_eq_6(self):
        node = TextNode("Hello", TextType.CODE, "https://www.boot.dev")
        node2 = TextNode("Hello", TextType.CODE, "https://www.bot.dev")
        self.assertEqual(node, node2)
'''
if __name__ == "__main__":
    unittest.main()