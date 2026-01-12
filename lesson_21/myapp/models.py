from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    def __str__(self):
        return self.title

from datetime import date
from django.db import models


class Blog(models.Model):
    # Nazwa bloga, krótki tekst
    name = models.CharField(max_length=100)
    # Opis / tagline bloga, dłuższy tekst
    tagline = models.TextField()

    def __str__(self):
        # Jak ten obiekt ma się wyświetlać jako tekst
        return self.name


class Author(models.Model):
    # Imię i nazwisko autora
    name = models.CharField(max_length=200)
    # Adres e‑mail autora
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    # Jeden wpis należy do jednego bloga
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    # Tytuł wpisu
    headline = models.CharField(max_length=255)
    # Treść wpisu
    body_text = models.TextField()
    # Data publikacji
    pub_date = models.DateField()
    # Data modyfikacji, domyślnie dziś
    mod_date = models.DateField(default=date.today)
    # Wielu autorów może napisać jeden wpis i odwrotnie
    authors = models.ManyToManyField(Author)
    # Liczba komentarzy
    number_of_comments = models.IntegerField(default=0)
    # Liczba pingbacków
    number_of_pingbacks = models.IntegerField(default=0)
    # Ocena wpisu (np. 1–10)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
