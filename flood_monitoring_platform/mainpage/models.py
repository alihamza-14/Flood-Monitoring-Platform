from django.contrib.gis.db import models

class FloodExtent(models.Model):
    geom = models.MultiPolygonField(srid=3857)  # Assuming MultiPolygonField for MVT

    def __str__(self):
        return f'FloodExtent object ({self.id})'

    class Meta:
        managed = False  # Ensure Django does not manage this table
        db_table = 'flood_june'  # Specify the actual table name in your database
