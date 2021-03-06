from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class JOB_POSTING(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    discription = models.TextField()
    contact = models.IntegerField()
    mail = models.EmailField()
    date = models.DateField(default=datetime.now,null=True)
    exp = models.IntegerField()
    location = models.CharField(max_length=20)
    employer = models.ForeignKey(User,on_delete=models.CASCADE)       #used to connecting the user table    
    def __str__(self):
        return self.title




class job_application(models.Model):
    user_applied = models.ForeignKey(User,on_delete=models.CASCADE)
    job_id = models.ForeignKey(JOB_POSTING,on_delete=models.CASCADE)
    applied_date = models.DateField(default=datetime.now,null=True)

    def __str__(self):
        return str(self.job_id)


class Create(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    discription = models.TextField()
    contact = models.IntegerField()
    mail = models.EmailField()
    exp = models.IntegerField()
    location = models.CharField(max_length=20)
    employer = models.ForeignKey(User,on_delete=models.CASCADE)       #used to connecting the user table

    def __str__(self):
        return self.title
"""
class post(models.Model):
    title= models.CharField(max_length=60)
    name= models.CharField(max_length=40)
    discription= models.TextField()
    contact=models.IntegerField()
    mail= models.EmailField()
    exp= models.IntegerField()
    location= models.CharField(max_length=40)
    datetime= models.datetime()

    def __str__(self):
        return self.title

"""
