from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import FloodExtentJuly, FloodExtentJune, FloodExtentAugust, Settlementsaug, Settlementsjune, Settlementsjuly, Settlementssept, Airportjune, Airportjuly, Airportaug, Airportsept, Pak
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
    
def settlements_aug(request):
    try:
        settlements = Settlementsaug.objects.all()
        geojson_data = get_flood_extent_data(settlements)  # You can reuse the helper function
        return JsonResponse(geojson_data)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})
    
def settlements_june(request):
    try:
        settlements = Settlementsjune.objects.all()
        geojson_data = get_flood_extent_data(settlements)  # You can reuse the helper function
        return JsonResponse(geojson_data)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})
    
def settlements_july(request):
    try:
        settlements = Settlementsjuly.objects.all()
        geojson_data = get_flood_extent_data(settlements)  # You can reuse the helper function
        return JsonResponse(geojson_data)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})

def settlements_sept(request):
    try:
        settlements = Settlementssept.objects.all()
        geojson_data = get_flood_extent_data(settlements)  # You can reuse the helper function
        return JsonResponse(geojson_data)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})
    
def airport_june(request):
    try:
        settlements = Airportjune.objects.all()
        geojson_data = get_flood_extent_data(settlements)  # You can reuse the helper function
        return JsonResponse(geojson_data)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})
    
def airport_july(request):
    try:
        settlements = Airportjuly.objects.all()
        geojson_data = get_flood_extent_data(settlements)  # You can reuse the helper function
        return JsonResponse(geojson_data)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})
    
def airport_aug(request):
    try:
        settlements = Airportaug.objects.all()
        geojson_data = get_flood_extent_data(settlements)  # You can reuse the helper function
        return JsonResponse(geojson_data)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})
    
def airport_sept(request):
    try:
        settlements = Airportsept.objects.all()
        geojson_data = get_flood_extent_data(settlements)  # You can reuse the helper function
        return JsonResponse(geojson_data)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})
    
def pak(request):
    try:
        settlements = Pak.objects.all()
        geojson_data = get_flood_extent_data(settlements)  # You can reuse the helper function
        return JsonResponse(geojson_data)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


def map_view(request):
    return render(request, 'mainpage/map.html')
