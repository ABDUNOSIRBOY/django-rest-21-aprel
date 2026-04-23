from django.db import models

# Create your models here.


class HotelRoom(models.Model):
    raqami = models.CharField(max_length=255)
    qavat = models.IntegerField(default=1)
    turi = models.CharField(max_length=255)
    narxi = models.CharField(max_length=255)
    band_holati = models.BooleanField(default=True)

    def __str__(self):
        return self.raqami


class Employee(models.Model):
    ismi = models.CharField(max_length=255)
    familiyasi = models.CharField(max_length=255)
    lavozimi = models.CharField(max_length=255)
    kirgan_sanasi = models.DateTimeField(auto_now_add=True)
    ish_haqi = models.CharField(max_length=255)

    def __str__(self):
        return self.ismi


class Movie(models.Model):
    nomi = models.CharField(max_length=255)
    janri = models.CharField(max_length=255)
    rejissyor = models.CharField(max_length=255)
    davomiyligi = models.CharField(max_length=255)
    chiqish_yili = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi