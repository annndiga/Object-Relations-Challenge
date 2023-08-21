from lib.article import Article
from lib.magazine import Magazine

class Author:
    def __init__(self,name):
        self.name = name
        self._articles = []
        self._magazines = [] 

    def write_article(self, title, magazine):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        magazine.add_article(new_article) 

    def write_magazine(self, name, category):
        new_magazine = Magazine(name, category)
        self._magazines.append(new_magazine)
        return new_magazine

    def __str__(self):
        article_details = "\n".join(str(article) for article in self._articles)
        magazine_details = "\n".join(str(magazine) for magazine in self._magazines)
        return f"Author: {self.name}\nArticles:\n{article_details}\nMagazines:\n{magazine_details}"
        