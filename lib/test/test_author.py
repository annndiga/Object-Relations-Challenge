import sys
import os
import unittest

# Adjust the path to the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from magazine.author import Author
from magazine.magazine import Magazine

class TestAuthor(unittest.TestCase):
    def setUp(self):
        self.author = Author("Brandy Makena")
        self.magazine1 = Magazine("Tech At the Moment", "Technology")
        self.magazine2 = Magazine("Gen Z on Health", "Health")

    def test_write_article(self):
        self.author.write_article("Python Basics", self.magazine1)
        self.assertEqual(len(self.author._articles), 1)
        self.assertEqual(self.author._articles[0].title, "Python Basics")
        self.assertEqual(self.author._articles[0].magazine, self.magazine1) 

    def test_write_magazine(self):
        self.author.write_magazine("Tech Today", "Technology")
        self.assertEqual(len(self.author._magazines), 1)
        self.assertEqual(self.author._magazines[0]._name, "Tech Today")

    def test_str_representation(self):
        self.author.write_article("Python Basics", self.magazine1)
        self.author.write_magazine("Tech Today", "Technology")
        expected_output = (
            "Author: Brandy Makena\n"
            "Articles:\n"
            "Article: Python Basics, Author: Brandy Makena, Magazine: Tech At the Moment\n"
            "Magazines:\n"
            "Magazine: Tech Today, Category: Technology"
        )
        self.assertEqual(str(self.author), expected_output)

if __name__ == '__main__':
    unittest.main()
