from django.db import models

# Create your models here.

class Teles_satel(models.Model):
    nom_tel_sat= models.CharField(max_length=40)
    edad_tel_sat= models.IntegerField()
    fechalanz_tel_sat= models.DateField()


class Teles_terr(models.Model):
    nom_tel_ter= models.CharField(max_length=40)
    edad_tel_ter= models.IntegerField()
    fechalanz_tel_ter= models.DateField()


class Teles_cur(models.Model):
    nom_tel_cur= models.CharField(max_length=40)
    edad_tel_cur= models.IntegerField()
    fechalanz_tel_cur= models.DateField()
