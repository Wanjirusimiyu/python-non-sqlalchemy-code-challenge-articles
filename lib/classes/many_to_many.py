class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if len(title) < 5:
            raise Exception("Title should be longer than 5 characters")
        if len(title) > 50:
            raise Exception("Title should not be longer than 50 characters")
        self._title = title
        self._author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if len(value) < 5:
            raise Exception("Title should be longer than 5 characters")
        if len(value) > 50:
            raise Exception("Title should not be longer than 50 characters")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise AttributeError("Author must be an instance of the Author class")
        self._author = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name cannot be an empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name cannot be an empty string")
        self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set([article.magazine.category for article in self.articles()]))

class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 2:
            raise Exception("Name must contain at least 2 characters")
        if len(name) > 16:
            raise Exception("Name should not contain more than 16 characters")
        if not isinstance(category, str):
            raise TypeError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category cannot be an empty string")
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 2:
            raise Exception("Name must contain at least 2 characters")
        if len(value) > 16:
            raise Exception("Name should not contain more than 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category cannot be an empty string")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        return [article.title for article in Article.all if article.magazine == self]
    

    def contributing_authors(self):
        authors = {}
        for article in Article.all:
          if article.magazine == self:
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        return [author.name for author, count in authors.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()))            