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

      Article._id += 1
      self.id = Article._id

    def short_introduction(self,n_characters : int):
      intro = list()
      j = 0
      i = n_characters
      while(self.content[i] != ' ' or self.content[i] != ' '):
        j += 1
        i -= 1

      if (self.content[n_characters + 1 ] == ' ' or self.content[n_characters + 1 ] == ' '):
        for i in range(n_characters):
          intro.append(self.content[i])
      else:
        for i in range(n_characters - j):
          intro.append(self.content[i])
      word = ''.join(intro)
      intro = "\"" + word + "\""
      print(intro)

    def __repr__(self):
      return '<Article title={title} author={author} publication_date={publication_date}>'.format(title=repr(self.title),author=repr(self.author),publication_date=repr(self.publication_date.isoformat()))

    def __len__(self):
      return (len(self.content))

fairytale = Article(
    title="The emperor's new clothes",
    author="Hans Christian Andersen",
    content="'But he has nothing at all on!' at last cried out all the people. The Emperor was vexed, for he knew that the people were right.",
    publication_date=datetime.datetime(1837, 4, 7, 12, 15, 0),
)

fairtale = Article(
    title="The emperor's new clothes",
    author="Hans Christian Andersen",
    content="'But he has nothing at all on!' at last cried out all the people. The Emperor was vexed, for he knew that the people were right.",
    publication_date=datetime.datetime(1837, 4, 7, 12, 15, 0),
)

print(fairytale.id)
print(fairtale.id)