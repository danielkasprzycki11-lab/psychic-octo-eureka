from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class Author(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='authors/', blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    publication_date = models.DateField(blank=True, null=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='books')

    def __str__(self):
        return self.title


class Copy(models.Model):
    STATUS_CHOICES = [
        ('available', 'Dostępny'),
        ('borrowed', 'Wypożyczony'),
        ('reserved', 'Zarezerwowany'),
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f'{self.book.title} ({self.get_status_display()})'


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE, related_name='reservations')
    reserved_at = models.DateField(auto_now_add=True)
    valid_until = models.DateField()

    def __str__(self):
        return f'{self.user.username} -> {self.copy}'
