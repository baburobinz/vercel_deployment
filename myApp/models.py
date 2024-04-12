from django.db import models
from django.contrib.auth.models import User


class UserMobile(models.Model):

    user= models.OneToOneField(User, on_delete=models.CASCADE)

    mobile = models.CharField(max_length=10)

    def __str__(self):
       
       return self.user.username



class to_do_list(models.Model):

    user_name = models.CharField(max_length=20)

    title = models.CharField(max_length=50)

    description = models.TextField(max_length=200)

    def __str__(self):

        return self.title