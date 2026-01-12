from django.db import models

# TO JEST KATEGORIA - jak działy w gazecie
class Category(models.Model):
    name = models.CharField(max_length=100)  # max_length=100 → nazwa może mieć maks 100 znaków
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"  # Nazwa w panelu admina

# TO JEST POST - artykuł na blogu
class Post(models.Model):
    title = models.CharField(max_length=200)  # Tytuł artykułu (maks 200 znaków)
    content = models.TextField()  # Treść artykułu (bez limitu)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # ← NOWE: artykuł należy do kategorii
    
    def __str__(self):
        return self.title
