from django.contrib.gis.db import models

# Create your models here.

class FloodExtentJuly(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'FloodExtentJuly object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'july'

class FloodExtentJune(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'FloodExtentJune object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'june'

class FloodExtentAugust(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'FloodExtentAugust object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'august'
