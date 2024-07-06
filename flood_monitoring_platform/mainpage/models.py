from django.contrib.gis.db import models

################################################################

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

################################################################

class PakAdministrativeBoundary(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'PakAdministrativeBoundary object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'pak_adm0'  # Replace with appropriate table name

################################################################

class NHARoadNetwork(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'NHARoadNetwork object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'nha_road_network_latest'  # Replace with appropriate table name

################################################################

class AugustAirport(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'AugustAirport object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'airportaug'  # Replace with appropriate table name


class JuneAirport(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'JuneAirport object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'airportjune'  # Replace with appropriate table name


class JulyAirport(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'JulyAirport object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'airportjuly'  # Replace with appropriate table name


class SeptemberAirport(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'SeptemberAirport object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'airportsept'  # Replace with appropriate table name



