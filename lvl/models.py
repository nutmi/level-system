from django.db import models
# Create your models here.
class LevelInformation(models.Model):
    needed_xp = models.IntegerField()