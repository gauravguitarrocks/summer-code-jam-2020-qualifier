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
      self.last_edited = None

      Article._id += 1
      self.id = Article._id

    def short_introduction(self,n_characters : int):
      self.content = self.content.replace('\n',' ')
      intro = list()
      j = 0
      i = n_characters
      while(ord(self.content[i]) != 32):
        j += 1
        i -= 1

      if (self.content[n_characters] == ' '):
        for i in range(n_characters):
          intro.append(self.content[i])
      else:
        for i in range(n_characters - j):
          intro.append(self.content[i])
      word = ''.join(intro)
      return word

    def __repr__(self):
      return '<Article title={title} author={author} publication_date={publication_date}>'.format(title=repr(self.title),author=repr(self.author),publication_date=repr(self.publication_date.isoformat()))

    def __len__(self):
      return (len(self.content))

    def __lt__(self,other):
      return self.publication_date < other.publication_date

    def most_common_words(self,rank: int):
      word = ''
      word_list = list()
      for i in range(len(self.content)):
        if ((int(ord(self.content[i])) > 64 and int(ord(self.content[i])) < 90) or (int(ord(self.content[i])) > 96 and int(ord(self.content[i])) < 123)):
          word += str(self.content[i])
        else:
          word = word.lower()
          word_list.append(word)
          word = ''
      word_list.append(word)
      length = len(word_list)
      i = 0
      while (i != length):
        if (word_list[i] == ''):
          word_list.remove(word_list[i])
          length -= 1
          continue
        i += 1
      word_frequency = list()
      for word_ in word_list:
        word_frequency.append(word_list.count(word_))
      word_dict = dict(zip(word_list,word_frequency))
      result = dict()
      for key,value in word_dict.items():
        if (key not in result.keys()):
          result[key] = value
      max_value = max(result.values())
      filtered_results = dict()
      while(max_value != -1):
        for key,value in result.items():
          if (value == max_value):
            filtered_results[key] = value
        max_value -= 1
      if (rank <= len(filtered_results)):
        return dict(list(filtered_results.items())[:rank])
      else:
        return dict(list(filtered_results.items())[:len(filtered_results)])

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
