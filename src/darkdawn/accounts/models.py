from django.contrib.auth import get_user_model
from django.db import models

user_model = get_user_model()
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        user_model, on_delete=models.CASCADE, related_name="profile"
    )
    is_member = models.BooleanField(default=False)