from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=10,null=True)
    role = models.CharField(max_length=15,null=True)

    # def __str__(self):
    #     return self.user.username


class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    uploadingdate = models.CharField(max_length=10,null=True)
    reportfile = models.FileField(null=True)
    filetype = models.CharField(max_length=30,null=True)
    description = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=30,null=True)

    # def __str__(self):
    #     return self.signup.user.username+" "+self.status


class Magazines(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    uploadedate = models.CharField(max_length=10,null=True)
    magazinesfile = models.FileField(null=True)
    magazinestype = models.CharField(max_length=30,null=True)
    description = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=30,null=True)

    # def __str__(self):
    #     return self.signup.user.username+" "+self.status

class Events(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    schedulename =models.CharField(max_length=25,null=True)
    eventtype= models.CharField(max_length=30,null=True)
    scheduledate=models.DateField(null=True)
    scheduletimefrom=models.TimeField(null=True)
    scheduletimeto=models.TimeField(null=True)
    scheduledDes=models.CharField(max_length=30,null=True)
class Vbaby(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    vtype= models.CharField(max_length=5,null=True)
    vname=models.CharField(max_length=30,null=True)
    vdur=models.CharField(max_length=30,null=True)
    vdose=models.CharField(max_length=30,null=True)
    vroute=models.CharField(max_length=30,null=True)
    vsite=models.CharField(max_length=30,null=True)
class Food(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name= models.CharField(max_length=5,null=True)
    image=models.FileField(null=True)
    description=models.CharField(max_length=30,null=True)
class Exercise(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name= models.CharField(max_length=5,null=True)
    video=models.FileField(null=True)
    description=models.CharField(max_length=30,null=True)
class Meditation(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name= models.CharField(max_length=5,null=True)
    video1=models.FileField(null=True)
    description=models.CharField(max_length=30,null=True)