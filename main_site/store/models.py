from django.db import models


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
    pub_date = models.DateField()
    approve_date = models.DateField(auto_now_add=True)
    rating = models.FloatField(default=0.0)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
