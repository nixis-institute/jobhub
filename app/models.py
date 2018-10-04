from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class JOB_POSTING(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    discription = models.TextField()
    contact = models.IntegerField()
    mail = models.EmailField()
    body = models.TextField()
    date = models.DateField()
    exp = models.IntegerField()
    location = models.CharField(max_length=20)
    employer = models.ForeignKey(User,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title
