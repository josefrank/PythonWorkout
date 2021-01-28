"""
A program that takes a list of dictionaries and sorts them by last name and
first name. In the book, there are multiple ways in which this problem could
be solved. But according to the author, this is the most efficient.
"""

from operator import itemgetter

PEOPLE = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump', 'email': 'president@whithouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'}]


def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts, key=itemgetter('last', 'first'))


print(alphabetize_names(PEOPLE))
