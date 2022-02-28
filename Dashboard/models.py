from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):   #class notes containning below 3 columns
    user = models.ForeignKey(User,on_delete=models.CASCADE)   #when this user is deleted then this notes also deleted from database
    title = models.CharField(max_length=200)
    description = models.TextField()