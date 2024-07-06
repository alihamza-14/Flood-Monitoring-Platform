from django.contrib.gis.db import models

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
        
class Settlementsaug(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Settlementsaug object ({self.id})'

    class Meta:
        db_table = 'settlementsaug'
        
class Settlementsjune(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Settlementsjune object ({self.id})'

    class Meta:
        db_table = 'settlementsjune'

class Settlementsjuly(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Settlementsjuly object ({self.id})'

    class Meta:
        db_table = 'settlementsjuly'
        
class Settlementssept(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Settlementssept object ({self.id})'

    class Meta:
        db_table = 'settlementssept'
        
class Airportjune(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Airportjune object ({self.id})'

    class Meta:
        db_table = 'airportjune'
        
class Airportjuly(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Airportjuly object ({self.id})'

    class Meta:
        db_table = 'airportjuly'
        
class Airportaug(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Airportaug object ({self.id})'

    class Meta:
        db_table = 'airportaug'
        
class Airportsept(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Airportsept object ({self.id})'

    class Meta:
        db_table = 'airportsept'
        
class Pak(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Pak object ({self.id})'

    class Meta:
        db_table = 'pak'
        
class Healthjune(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Healthjune object ({self.id})'

    class Meta:
        db_table = 'healthjune'
        
class Healthjuly(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Healthjuly object ({self.id})'

    class Meta:
        db_table = 'healthjuly'
        
class Healthaug(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Healthaug object ({self.id})'

    class Meta:
        db_table = 'healthaug'
        
class Healthsept(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Healthsept object ({self.id})'

    class Meta:
        db_table = 'healthsept'
        
class Schooljune(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Schooljune object ({self.id})'

    class Meta:
        db_table = 'schooljune'
        
class Schooljuly(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Schooljuly object ({self.id})'

    class Meta:
        db_table = 'schooljuly'
        
class Schoolaug(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Schoolaug object ({self.id})'

    class Meta:
        db_table = 'schoolaug'
        
class Schoolsept(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Schoolsept object ({self.id})'

    class Meta:
        db_table = 'schoolsept'
        
class Nharoads(models.Model):
    geom = models.PolygonField()

    def __str__(self):
        return f'Nharoads object ({self.id})'

    class Meta:
        db_table = 'nharoads'