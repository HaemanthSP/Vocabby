"""Module to prepare and maintain book for vocabulary learning."""
import pickle

from vocab_builder import Vocab
from random import randint


class Book:
    """Prepare a book for reading."""

    def __init__(self, text, title, author, gener, year, publisher, code):
        self.text = text
        self.title = title
        self.author = author
        self.gener = gener
        self.year = year
        self.publisher = publisher
        self.code = code
        self.vocab = Vocab(text)
        self.words = self.vocab.words
        self.families = self.vocab.families
        self.network = self.vocab.network

    def get_stats(self):
        """Get the statistics on vocabulary of the book."""
        stats = self.vocab.stats()
        return stats

    @staticmethod
    def load(book_code):
        """Loads the processed book from shelf."""
        with open('books/' + book_code + '.p', 'rb') as book_file:
            book = pickle.load(book_file)
        return book

    def save(self):
        """Save the book for future use."""
        with open('books/' + self.code + '.p', 'wb') as book_file:
            pickle.dump(self, book_file)


class Bookshelf:
    """Organizes book for future learners to fetch."""

    def __init__(self, name):
        self.name = name
        self.book_codes = {}

    def add_book(self, text, title, author, gener, year, publisher):
        """Add a new book to the shelf."""
        code = self._generate_code(title, author, year)

        if self.find_book(self, text, title, author, gener, year, publisher):
            return

        self.book_codes.update(
                {code: {'title': title,
                        'author': author,
                        'gener': gener,
                        'year': year,
                        'publisher': publisher}})
        book = Book(text, title, author, gener, year, publisher, code)
        book.save()

    def _generate_code(self, title, author, year):
        """Generate a unique code for the book."""
        samples = [self.name[:4], title[:5], author[:5],
                   year[:4], str(randint(0, 9999))]

        return '_'.join(samples)

    def find_book(self, *args):
        """Find whether a book exists in the shelf."""
        # raise NotImplementedError
        return None

    def get_book(self, book_code):
        """Get the book corresponding to the code."""
        return Book.load(book_code)

    @staticmethod
    def load(shelf_name):
        """Loads the processed book from shelf."""
        with open('books/' + shelf_name + '.p', 'rb') as shelf_file:
            book = pickle.load(shelf_file)
        return book

    def save(self):
        """Save the book for future use."""
        with open('books/' + self.name + '.p', 'wb') as shelf_file:
            pickle.dump(self, shelf_file)
