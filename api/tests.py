from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Author, Book, Page

class AuthorModelTest(TestCase):
    def test_author_creation(self):
        User = get_user_model()
        user = User.objects.create_user(username='author1', password='test123', is_author=True)
        author = Author.objects.create(user=user)

        self.assertEqual(author.user.username, 'author1')
        self.assertTrue(author.user.is_author)


class ReaderModelTest(TestCase):
    def test_reader_creation(self):
        User = get_user_model()
        user = User.objects.create_user(username='reader1', password='test123', is_author=False)

        self.assertEqual(user.username, 'reader1')
        self.assertFalse(user.is_author)

class AuthorManageBookAndPageTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.author_user = User.objects.create_user(username='author1', password='test123', is_author=True)
        self.reader_user = User.objects.create_user(username='reader1', password='test123', is_author=False)
        
        self.author = Author.objects.create(user=self.author_user)
        self.book = Book.objects.create(title='Test Book', brief='This is a test book', author=self.author)
        self.page = Page.objects.create(content='Test page content', book=self.book)

    def test_author_can_create_book(self):
        self.assertEqual(self.author.books.count(), 1)

    def test_author_can_create_page(self):
        self.assertEqual(self.book.pages.count(), 1)

    def test_reader_cannot_create_book(self):
        response = self.client.post('/api/books/', {'title': 'New Book', 'brief': 'This is a new book', 'author': self.reader_user.pk})
        self.assertEqual(response.status_code, 401)

    def test_reader_cannot_create_page(self):
        response = self.client.post('/api/pages/', {'content': 'New page content', 'book': self.book.pk})
        self.assertEqual(response.status_code, 404)
