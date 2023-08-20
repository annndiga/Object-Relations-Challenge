class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine._all_magazines.append(self)

    def add_article(self, article):
        self._articles.append(article)

    def __str__(self) -> str:
        return f"Magazine: {self._name}, Category: {self._category}"