from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import FloodExtentJuly, FloodExtentJune, FloodExtentAugust
from django.contrib.gis.geos import GEOSGeometry

def get_flood_extent_data(flood_extents):
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
    return {
        "type": "FeatureCollection",
        "features": features
    }

def flood_extent_july(request):
    try:
        flood_extents = FloodExtentJuly.objects.all()
        geojson_data = get_flood_extent_data(flood_extents)
        return JsonResponse(geojson_data)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})

def flood_extent_june(request):
    try:
        flood_extents = FloodExtentJune.objects.all()
        geojson_data = get_flood_extent_data(flood_extents)
        return JsonResponse(geojson_data)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})

def flood_extent_august(request):
    try:
        flood_extents = FloodExtentAugust.objects.all()
        geojson_data = get_flood_extent_data(flood_extents)
        return JsonResponse(geojson_data)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})

def map_view(request):
    return render(request, 'mainpage/map.html')
