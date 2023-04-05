from django.db import models



class signup(models.Model):
    name = models . CharField(max_length=255)
    email = models . CharField(max_length=255)
    password = models . CharField(max_length= 255)

class login (models.Model):
    Username = models . CharField(max_length=255)
    password = models . CharField(max_length=255)

