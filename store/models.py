from django.db import models
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFill
# from django.utils.text import slugify
from uuid import uuid4
import os


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

    def get_file_path(self, filename):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid4(), extension)
        return os.path.join("images/covers", filename)

    name = models.CharField(max_length=200)
    coverpic = models.ImageField(upload_to=get_file_path, default='images/default_book_pic.png')
    coverpic_small = ImageSpecField(source='coverpic', processors=[ResizeToFill(100, 100)], format='JPEG', options={'quality': 60})
    pub_date = models.DateField()           # publication date NEED CHANGE FOR ONLY YEARt
    approve_date = models.DateTimeField(auto_now_add=True)      # date of applying book on this site
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
