from datetime import datetime
from django.db import models
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify
from uuid import uuid4
import os


class Genre(models.Model):

    def __str__(self):
        return self.name

    def get_last_book(self):
        return self.books.order_by('-approve_date')[0]

    name = models.CharField(max_length=200)


class Author(models.Model):

    def __str__(self):
        return self.name

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


class Book(models.Model):

    YEAR_CHOICES = []
    for r in range(1900, datetime.now().year + 1):
        YEAR_CHOICES.append((r, r))

    def get_file_path(self, filename):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid4(), extension)
        return os.path.join("images/covers", filename)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = '%s-%i' % (slugify(self.name), self.pub_date)
        super(Book, self).save(*args, **kwargs)

    name = models.CharField(max_length=200)
    coverpic = models.ImageField(upload_to=get_file_path,
                                 default='images/default_book_pic.png')
    coverpic_small = ImageSpecField(source='coverpic',
                                    processors=[ResizeToFill(100, 100)],
                                    format='JPEG', options={'quality': 60})
    pub_date = models.SmallIntegerField(_('year'), max_length=4,
                                        choices=YEAR_CHOICES, default=1900)
    approve_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, related_name='books',
                              on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    slug = models.SlugField()
