from django.db import models
class Bookinfo(models.Model):
    P_name=models.CharField(max_length=40)
    Num_p=models.IntegerField()
    Arriv_d=models.DateField()
    Leav_d=models.DateField()
    def __str__(self) :
        return self.P_name

class continfo(models.Model):
    Name=models.CharField(max_length=40)
    P_num=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()
    def __str__(self) :
        return self.Name
        
class loginfo(models.Model):
    user_email=models.EmailField(max_length=40)
    user_pass=models.CharField(max_length=40)
    def __str__(self):
        return self.user_email


# Create your models here.
