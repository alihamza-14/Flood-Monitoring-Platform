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
        db_table = 'pakistan_shapfile'  # Replace with appropriate table name

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

###################################################################

class JuneHealth(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'JuneHealth object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'healthjune'  # Replace with appropriate table name

class JulyHealth(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'JulyHealth object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'healthjuly'  # Replace with appropriate table name

class AugustHealth(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'AugustHealth object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'healthaug'  # Replace with appropriate table name

class SeptemberHealth(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'SeptemberHealth object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'healthsept'  # Replace with appropriate table name

########################################################################

class AugustRoads(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'AugustRoads object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'aug_roads'  # Replace with appropriate table name

class JuneRoads(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'JuneRoads object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'june_roads'  # Replace with appropriate table name

class JulyRoads(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'JulyRoads object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'july_roads'  # Replace with appropriate table name

class SeptemberRoads(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'SeptemberRoads object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'sept_roads'  # Replace with appropriate table name

###########################################################################

class SettlementsAug(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'SettlementsAug object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'settlementsaug'  # Replace with appropriate table name

class SettlementsJune(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'SettlementsJune object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'settlementsjune'  # Replace with appropriate table name

class SettlementsJuly(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'SettlementsJuly object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'settlementsjuly'  # Replace with appropriate table name

class SettlementsSept(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'SettlementsSept object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'settlementssept'  # Replace with appropriate table name

#############################################################

class SchoolsAug(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'SchoolsAug object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'schoolaug'  # Replace with appropriate table name

class SchoolsJune(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'SchoolsJune object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'schooljune'  # Replace with appropriate table name

class SchoolsJuly(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'SchoolsJuly object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'schooljuly'  # Replace with appropriate table name

class SchoolsSept(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'SchoolsSept object ({self.id})'

    def get_area(self):
        return self.geom.area

    class Meta:
        db_table = 'schoolsept'  # Replace with appropriate table name

