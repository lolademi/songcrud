from django.db import models


class Artiste(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    age = models.IntegerField()

    def __str__(self):
        return self.firstname


class Song(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Lyrics(models.Model):
    content = models.TextField()
    song_id = models.IntegerField()
    song_title = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
