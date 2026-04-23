from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=100)
    yonalishi = models.CharField(max_length=255)
    ochilgan_sana = models.DateTimeField(auto_now_add=True)
    talabalar_soni = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class Course(models.Model):
    nomi = models.CharField(max_length=255)
    narxi = models.IntegerField(default=0)
    davomiyligi = models.IntegerField(default=0)  
    darajasi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class Subject(models.Model):
    nomi = models.CharField(max_length=255)
    dars_soati = models.IntegerField(default=120)
    laboratoriya_borligi = models.BooleanField(default=True)

    def __str__(self):
        return self.nomi

