from django.contrib.gis.db import models

# Create your models here.

class FloodExtent(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'FloodExtent object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'june'