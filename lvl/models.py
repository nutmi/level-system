from django.db import models


# Create your models here.
class LevelInformation(models.Model):
    level = models.IntegerField(default=0)
    needed_xp = models.IntegerField()
