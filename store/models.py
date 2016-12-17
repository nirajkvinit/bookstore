from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    M = 'Male'
    F = 'Fem'
    GENDER_CHOICES = (
        (M, 'Male'),
        (F, 'Female'),
    )
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    gender = models.CharField(max_length=4,
                              choices=GENDER_CHOICES,
                              default='Male')

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateField()           # publication date
    approve_date = models.DateTimeField(auto_now_add=True)      # date of applying book on this app
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    favorites_by = models.ManyToManyField(User)

    def __str__(self):
        return self.name
