import pdb; pdb.set_trace()  # XXX BREAKPOINT
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)


class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    gender = models.DateField()


class Book(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateField()
    approve_date = models.DateField()
    rating = models.FloatField()
    genre = models.ForeignKey(Genre)
    author = models.ForeignKey(Author)
# Create your models here.
