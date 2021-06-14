from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Snacks(models.Model):
    name = models.CharField(max_length=256)
    purcheser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()
    def __str__(self):
        return self.name

