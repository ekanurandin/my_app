from django.db import models

# Create your models here.

class Beranda(models.Model):
    nama = models.CharField(max_length=225)
    keterangan = models.TextField()

    def __str__(self):
        return f"{self.nama}"

class Menu(models.Model):
    nama = models.CharField(max_length=225)
    keterangan = models.TextField()
    
    def __str__(self):
        return f"{self.nama}"