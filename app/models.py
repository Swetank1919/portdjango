from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(null=True)


    def __str__(self):
        return self.title

class Skill(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=300)



    def __str__(self):
        return self.title
class Message(models.Model):
    name=models.CharField(max_length=100)
    message=models.CharField(max_length=1000)

    def __str__(self):
        return self.name

   