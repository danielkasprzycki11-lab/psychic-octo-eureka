from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Author, Genre, Book, Copy


class ModelsTestCase(TestCase):
    def test_create_book_and_copy(self):
        author = Author.objects.create(name="Test Author")
        genre = Genre.objects.create(name="Test Genre")
        book = Book.objects.create(
            title="Test Book",
            description="Opis testowy",
            publication_date=date(2020, 1, 1),
            author=author,
            genre=genre,
        )
        copy = Copy.objects.create(book=book, status="available")

        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Copy.objects.count(), 1)
        self.assertEqual(copy.book.title, "Test Book")


class ViewsTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Autor Widoku")
        self.genre = Genre.objects.create(name="Gatunek Widoku")
        self.book1 = Book.objects.create(
            title="Python dla początkujących",
            description="Książka o Pythonie.",
            publication_date=date(2021, 5, 1),
            author=self.author,
            genre=self.genre,
        )
        self.book2 = Book.objects.create(
            title="Zaawansowane Django",
            description="Django na poważnie.",
            publication_date=date(2022, 1, 1),
            author=self.author,
            genre=self.genre,
        )

    def test_book_list_status_code(self):
        url = reverse('library:book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python dla początkujących")
        self.assertContains(response, "Zaawansowane Django")

    def test_book_list_search(self):
        url = reverse('library:book_list')
        response = self.client.get(url, {'q': 'Python'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python dla początkujących")
        self.assertNotContains(response, "Zaawansowane Django")
