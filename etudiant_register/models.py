from django.db import models

# Create your models here.

class Evenement(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Etudiant(models.Model):
    name = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    mobile= models.CharField(max_length=15)
    evenement= models.ForeignKey(Evenement,on_delete=models.CASCADE)