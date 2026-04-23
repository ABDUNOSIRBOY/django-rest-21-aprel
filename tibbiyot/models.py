from django.db import models

# Create your models here.




class Doctor(models.Model):
    ismi = models.CharField(max_length=255)
    familiyasi = models.CharField(max_length=255)
    mutaxassisligi = models.CharField(max_length=255)
    xona_raqami = models.CharField(max_length=255)
    tajribasi = models.IntegerField(default=0)

    def __str__(self):
        return self.ismi


class Patient(models.Model):
    ismi = models.CharField(max_length=255)
    familiyasi = models.CharField(max_length=255)
    kasallik_tarixi = models.CharField(max_length=255)
    qon_guruhi = models.CharField(max_length=255)
    yoshi = models.IntegerField(default=0)

    def __str__(self):
        return self.ismi


class Appointment(models.Model):
    sana = models.DateField(auto_now_add=True)
    vaqt = models.TimeField(auto_now_add=True)
    shikoyati = models.CharField(max_length=255)

    def __str__(self):
        return self.sana


class Medicine(models.Model):
    nomi = models.CharField(max_length=255)
    dozasi = models.CharField(max_length=255)
    turi = models.CharField(max_length=255)
    muddati = models.CharField(max_length=255)
    qollash_usuli = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi
