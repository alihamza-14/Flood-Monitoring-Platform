from django.contrib.gis.db import models

class June(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'June object ({self.id})'

    class Meta:
        db_table = 'june'

class July(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'July object ({self.id})'

    class Meta:
        db_table = 'july'

class August(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'August object ({self.id})'

    class Meta:
        db_table = 'aug'

class September(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'September object ({self.id})'

    class Meta:
        db_table = 'sep'
