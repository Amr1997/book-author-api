from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_author = models.BooleanField(default=False)

class Author(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class Book(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='book_images/')
    brief = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE , related_name='books')

class Page(models.Model):
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE , related_name='pages')
