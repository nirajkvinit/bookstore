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
    pub_date = models.DateField()           # publication date
    approve_date = models.DateTimeField(auto_now_add=True)      # date of applying book on this app
    # rating = models.FloatField(default=0.0)
    # votes = models.IntegerField(default=0)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    # def upd_rating(self, new_vote):
        # print("Start method UPD_RATING")
        # print('new vote', new_vote)
        # if new_vote in range(1, 6):
            # # print('need to update')
            # new_rating = (self.rating * self.votes + new_vote)/(self.votes + 1)
            # self.votes += 1
            # # print("now vote is incremented")
            # self.rating = new_rating
            # self.save(update_fields=['rating', 'votes'])
            # print("UPDATED")
