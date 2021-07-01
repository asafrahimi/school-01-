from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=20)
    album_title = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    def __str__(self):
        return self.artist + 'and' + self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    #num_song = models.IntegerField()
    file_type = models.CharField(max_length=20)
    song_title = models.CharField(max_length=20)
