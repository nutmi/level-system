from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Quest(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    quest_answer = models.SlugField(max_length=50)
    xp = models.IntegerField()

    def __str__(self) -> str:
        return self.title


class QuestComplite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    answer = models.SlugField(max_length=50)
