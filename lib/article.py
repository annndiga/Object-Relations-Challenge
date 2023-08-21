

class Article:
    _all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article._all_articles.append(self)
  
    def author(self):
        return self._author

    def magazine(self):
        return self._magazine

    def title(self):
        return self._title

    @classmethod
    def all(cls):
        return Article._all_articles

    def __str__(self):
        return f"Article: {self.title}, Author: {self.author.name}, Magazine: {self.magazine._name}"