from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import FloodExtent

from django.contrib.gis.geos import GEOSGeometry


def flood_extent(request):
    try:
        flood_extents = FloodExtent.objects.all()
        features = []
        for extent in flood_extents:
            geom = GEOSGeometry(extent.geom.wkt)
            features.append({
                "type": "Feature",
                "geometry": geom.geojson,
                "properties": {
                    "id": extent.id,
                    # Add other properties here if needed
                }
            })
        geojson_data = {
            "type": "FeatureCollection",
            "features": features
        }
        return JsonResponse(geojson_data)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


def map_view(request): 
    return render(request,'mainpage/map.html')
