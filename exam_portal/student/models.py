from django.db import models

class user_data(models.Model):
    email=models.CharField(max_length=255 )
    password=models.CharField(max_length=255)
    confirm_password=models.CharField(max_length=255)
    age=models.IntegerField()
    gender=models.CharField(max_length=255)
    studying_year=models.IntegerField(max_length=255)
    DateofBirth=models.DateField()
    def __str__(self):
        return self.email