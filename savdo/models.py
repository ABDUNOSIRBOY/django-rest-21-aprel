from django.db import models

# Create your models here.




class Product(models.Model):
    nomi = models.CharField(max_length=255)
    kodi = models.CharField(max_length=255)
    narxi = models.IntegerField(default=0)
    miqdori = models.IntegerField(default=0)
    ishlab_chiqaruvchi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class Category(models.Model):
    nomi = models.CharField(max_length=255)
    tavsifi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi




class Customer(models.Model):
    ismi = models.CharField(max_length=255)
    familiyasi = models.CharField(max_length=255)
    telefon = models.CharField(max_length=255)
    manzili = models.CharField(max_length=255)
    jami_xaridi = models.IntegerField(default=0)


    def __str__(self):
        return self.ismi


class Order(models.Model):
    sana = models.DateTimeField(auto_now_add=True)
    umumiy_summa = models.CharField(max_length=255)
    tolov_turi = models.CharField(max_length=255)

    def __str__(self):
        return self.sana


class Supplier(models.Model):
    kompaniya_nomi = models.CharField(max_length=255)
    masul_shaxs = models.CharField(max_length=255)
    telefon = models.CharField(max_length=255)
    yetkazish_muddati = models.IntegerField(default=1000000000)


    def __str__(self):
        return self.kompaniya_nomi