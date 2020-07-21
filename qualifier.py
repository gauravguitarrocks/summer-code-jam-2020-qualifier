"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing
from collections import Counter
import re


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""
    _id = -1

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
      self.title = title
      self.author = author
      self.publication_date = publication_date
      self.content = content
      self.last_edited = None

      Article._id += 1
      self.id = Article._id

    def short_introduction(self,n_characters : int):
      self.content = self.content.replace('\n',' ')
      count = 0
      for i in range(n_characters):
        if self.content[i] == ' ':
          count +=1
      return ' '.join(self.content.split()[:count])

    def __repr__(self):
      return f"<Article title={repr(self.title)} author={repr(self.author)} publication_date={repr(self.publication_date.isoformat())}>"

    def __len__(self):
      return (len(self.content))

    def __lt__(self,other):
      return self.publication_date < other.publication_date

    def __setattr__(self,name,value):
      if name == 'content':
        self.last_edited = datetime.datetime.now()
      super().__setattr__(name,value)

    def most_common_words(self,rank: int):
      content = re.sub('[\W_]+',' ',self.content.lower())
      counter = Counter(content.split())
      word_list =  counter.most_common(rank)
      common_words = dict()
      for a,b in word_list:
        common_words[a] = b
      return common_words


# fairytale = Article(
#     title="The emperor's new clothes",
#     author="Hans Christian Andersen",
#     content="All the town",
#     publication_date=datetime.datetime(1837, 4, 7, 12, 15, 0),
# )

# fairtale = Article(
#     title="The emperor's new clothes",
#     author="Hans Christian Andersen",
#     content="see anything.\nHis whole",
#     publication_date=datetime.datetime(1837, 4, 7, 12, 15, 0),
# )

# print(fairytale.id)
# print(fairtale.last_edited)
# print(fairytale.most_common_words(3))
# print(ord('t'))
# print(ord(fairytale.content[0]))
# print(ord(' '))
# print(fairtale.short_introduction(16))
# print(str(fairtale.content.replace('\n',chr(32))))

# articles = [
#   Article(
#     title="The emperor's new clothes",
#     author="Hans Christian Andersen",
#     content="see anything.\nHis whole",
#     publication_date=datetime.datetime(2001, 7, 5),
# ),
# Article(
#     title="The emperor's new clothes",
#     author="Hans Christian Andersen",
#     content="see anything.\nHis whole",
#     publication_date=datetime.datetime(1837, 4, 7),
# ),
# Article(
#     title="The emperor's new clothes",
#     author="Hans Christian Andersen",
#     content="see anything.\nHis whole",
#     publication_date=datetime.datetime(2015, 8, 20),
# )
# ]

# print(sorted(articles))
