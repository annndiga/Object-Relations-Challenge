

class Article:
    _all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article._all_articles.append(self)
  
    def title(self):
        return self._title

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine

    @classmethod
    def all(cls):
        return cls._all_articles

    def __str__(self):
        return f"Article: {self._title}, Author: {self._author.name}, Magazine: {self._magazine.name}"