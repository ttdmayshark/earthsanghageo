from django.contrib.gis.db import models

class Genus(models.Model):
    name = models.CharField()

class Species(models.Model):
    name = models.CharField()
    common_name = model.CharField()
    genus = models.ForeignKey(Genus)

class Plant(models.Model):
    date_created = models.DateField()
    location = models.PointField()
