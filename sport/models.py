from django.db import models

# Create your models here.


class Athlete(models.Model):
    ismi = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    sport_turi = models.CharField(max_length=255)
    boyi = models.CharField(max_length=255)
    vazni = models.CharField(max_length=255)

    def __str__(self):
        return self.ismi


class Gym(models.Model):
    nomi = models.CharField(max_length=255)
    manzili = models.CharField(max_length=255)
    oylik_abonement_narxi = models.CharField(max_length=255)
    ish_vaqti = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class Competition(models.Model):
    nomi = models.CharField(max_length=255)
    sana = models.DateField(auto_now_add=True)
    mukofot_jamgarmasi = models.CharField(max_length=255)
    manzili = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class Coach(models.Model):
    ismi = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    tajribasi = models.IntegerField(default=True)
    ixtisosligi = models.CharField(max_length=255)
    oylik_maosh = models.CharField(default=0)
