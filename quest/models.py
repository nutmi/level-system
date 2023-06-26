from django.db import models

# Create your models here.
class Quest(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    quest_answer = models.SlugField(max_length=50)
    xp = models.IntegerField()

    def __str__(self) -> str:
        return self.title