from django.contrib.gis.db import models

class JuneFloodExtent(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'JuneFloodExtent object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'june'  # Replace with appropriate table name

class SeptemberFloodExtent(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'SeptemberFloodExtent object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'sep'  # Replace with appropriate table name

class JulyFloodExtent(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'JulyFloodExtent object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'july'  # Replace with appropriate table name

class AugustFloodExtent(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'AugustFloodExtent object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'aug'  # Replace with appropriate table name
