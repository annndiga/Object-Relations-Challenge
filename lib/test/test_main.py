import pytest
from magazine.author import Author
from magazine.magazine import Magazine
from magazine.article import Article

@pytest.fixture
def setup_authors_and_magazines():
    author1 = Author("Brandy Makena")
    author2 = Author("Kyle Njuki")
    
    magazine1 = Magazine("Tech At the Moment", "Technology")
    magazine2 = Magazine("Gen Z on Health", "Health")
    
    author1.write_article("Python Basics", magazine1)
    author2.write_article("Machine Learning", magazine1)
    author2.write_article("Healthy Habits", magazine2)
    
    author1.write_magazine("Tech Today", "Technology")
    author2.write_magazine("Health Weekly", "Health")
    
    return author1, author2, magazine1, magazine2

def test_author_str(setup_authors_and_magazines):
    author1, author2, _, _ = setup_authors_and_magazines
    expected_output = "Author: Brandy Makena\nArticles:\nArticle: Python Basics, Author: Brandy Makena, Magazine: Tech At the Moment\nMagazines:\nMagazine: Tech Today, Category: Technology"
    assert str(author1) == expected_output

def test_magazine_str(setup_authors_and_magazines):
    _, _, magazine1, _ = setup_authors_and_magazines
    expected_output = "Magazine: Tech At the Moment, Category: Technology"
    assert str(magazine1) == expected_output