from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Guess(models.Model):
    number=models.IntegerField()

    