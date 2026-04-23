from django.db import models

# Create your models here.


class Car(models.Model):
    markasi = models.CharField(max_length=255)
    modeli = models.CharField(max_length=255)
    rangi = models.CharField(max_length=255)
    davlat_raqami = models.CharField(max_length=255)
    yili = models.IntegerField(default=1850)

    def __str__(self):
        return self.markasi


class Driver(models.Model):
    ismi = models.CharField(max_length=255)
    familiyasi = models.CharField(max_length=255)
    guvohnoma_toifasi = models.CharField(max_length=255)
    tajribasi = models.IntegerField(default=0)
    reytingi = models.IntegerField(default=0)

    def __str__(self):
        return self.ismi


class Route(models.Model):
    boshlangich_nuqta = models.CharField(max_length=255)
    yakuniy_nuqta = models.CharField(max_length=255)
    masofa = models.CharField(max_length=255)
    davomiyligi = models.CharField(max_length=255)

    def __str__(self):
        return self.boshlangich_nuqta