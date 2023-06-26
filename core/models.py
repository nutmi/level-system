from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    gained_xp = models.IntegerField(default=0)
    level = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.user)