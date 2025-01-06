import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "Hello", None, {"href": "https://www.google.com", "target": "blank"})
        node2 = HTMLNode("a", "Hello", None, {"href": "https://www.google.com", "target": "blank"})
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)
    
    def test_eq_3(self):
        node = HTMLNode("a")
        node2 = HTMLNode("a")
        self.assertEqual(node, node2)

    def test_eq_4(self):
        node = LeafNode("This is a paragraph of text.", "p")
        node2 = LeafNode("Click me!", "a",{"href": "https://www.google.com"})
        print(node.to_html())
        print(node2.to_html())

    def test_eq_5(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text"),])
        print(f"this is result of node.tohtml(): {node.to_html()}")

    def test_eq_6(self):
        node = ParentNode("p", [ParentNode("b", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text"),]), LeafNode("i", "italic text")])
        print(f"this is result of node.tohtml(): {node.to_html()}")
    
    def test_eq_7(self):
        node = ParentNode("p", [LeafNode("b", "hi")])
        print(f"this is result of node.tohtml(): {node.to_html()}")
if __name__ == "__main__":
    unittest.main()