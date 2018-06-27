from django.db import models
from django.db.models import Model

# Create your models here.


class UserProfile(Model):
    """
    Database definition for user profile class
    """
    email_id = models.CharField(primary_key=True,max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()