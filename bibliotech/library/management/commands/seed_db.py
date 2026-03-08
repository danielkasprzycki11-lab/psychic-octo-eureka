import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from library.models import Author, Genre, Book, Copy
from datetime import date, timedelta
import random

fake = Faker('pl_PL')


class Command(BaseCommand):
    help = 'Wypełnia bazę danymi testowymi'

    def handle(self, *args, **options):
        # Usuń stare dane
        Copy.objects.all().delete()
        Book.objects.all().delete()
        Author.objects.all().delete()
        Genre.objects.all().delete()

        # Gatunki
        genres = ['Fantasy', 'Kryminał', 'Romans', 'Sci-Fi', 'Historyczna']
        for name in genres:
            Genre.objects.get_or_create(name=name)

        # Autorzy (5)
        authors = []
        for _ in range(5):
            author = Author.objects.create(
                name=fake.name(),
            )
            authors.append(author)

        # Książki (15)
        genres_all = Genre.objects.all()
        for _ in range(15):
            book = Book.objects.create(
                title=fake.sentence(nb_words=4)[:-1],  # Bez kropki
                description=fake.paragraph(nb_sentences=3),
                publication_date=fake.date_between(start_date='-10y', end_date='today'),
                author=random.choice(authors),
                genre=random.choice(genres_all)
            )

            # 1-3 egzemplarze na książkę
            for _ in range(random.randint(1, 3)):
                Copy.objects.create(
                    book=book,
                    status=random.choice(['available', 'reserved'])
                )

        self.stdout.write(self.style.SUCCESS('Dane testowe wygenerowane!'))
