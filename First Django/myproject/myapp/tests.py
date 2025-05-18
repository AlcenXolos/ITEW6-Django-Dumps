from django.test import TestCase
from .models import Book
class BookModelTest(TestCase):
    def test_book_creation(self):
        book = Book.objects.create(
            title="Test Book",
            author="Author Name",
            published_date="2023-10-10",
            isbn="1234567890123",
            pages=200
        )
        self.assertTrue(isinstance(book, Book))
        self.assertEqual(book.__str__(), book.title)