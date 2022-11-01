from django.db import models


class Artise(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.firstname


class Song(models.Model):
    title = models.CharField(max_length=20)
    date_released = models.DateField()
    likes = models.IntegerField()

    def __str__(self):
        return self.title


class Lyric(models.Model):
    content = models.TextField()
    song_id = models.IntegerField()

    def __str__(self):
        return self.content

