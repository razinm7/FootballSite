from datetime import datetime
# Create your models here.
from django.db import models


class Player(models.Model):
    player_name = models.CharField(max_length=50, default=None, null=True)
    player_dob = models.DateField(default=None, null=True)
    player_country = models.CharField(max_length=50, default=None, null=True)
    player_curr_team = models.CharField(max_length=50, default=None, null=True)
    player_curr_team_link = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True, null=True)
    player_position = models.CharField(max_length=50, default=None, null=True)
    player_photo = models.ImageField(upload_to="gallery", default=None, null=True, blank=True)


# типы полей бывают самые разные - числа, время, даты, bool, ссылки, файлы, картинки...
# а у нас models.TextField() просто текстовое поле произвольного размера

class Team(models.Model):
    team_name = models.CharField(max_length=50, default=None)
    stadium = models.CharField(max_length=50, default=None)
    est_year = models.IntegerField(default=None)
    curr_trainer = models.CharField(max_length=50, default=None)
    UEFA_rate = models.IntegerField(default=None)
    emblem = models.ImageField(upload_to="gallery", default=None, blank=True)

    def __str__(self):
        return self.team_name
