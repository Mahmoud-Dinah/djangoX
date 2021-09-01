from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Snack(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(default='')
    purchaser = models.ForeignKey(get_user_model(),related_name='snacks',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

