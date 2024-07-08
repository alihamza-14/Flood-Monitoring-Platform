from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import JuneFloodExtent, SeptemberFloodExtent, JulyFloodExtent, AugustFloodExtent, PakAdministrativeBoundary, JuneAirport, JulyAirport, AugustAirport, SeptemberAirport, NHARoadNetwork, JuneHealth, JulyHealth, AugustHealth, SeptemberHealth, JuneRoads, JulyRoads, AugustRoads, SeptemberRoads, SettlementsJune, SettlementsJuly, SettlementsAug, SettlementsSept, SchoolsJune, SchoolsJuly, SchoolsAug, SchoolsSept
from django.contrib.gis.geos import GEOSGeometry
from django.core.cache import cache

def flood_extent(request):
    try:
        if 'month' in request.GET:
            month = request.GET['month']
            cache_key = f'flood_extents_{month}'  # Define a cache key based on the month parameter

            # Attempt to fetch cached data first
            cached_data = cache.get(cache_key)
            if cached_data:
                return JsonResponse(cached_data)

            # If data is not cached, fetch and cache it
            if month == 'june':
                flood_extents = list(JuneFloodExtent.objects.all())
            elif month == 'september':
                flood_extents = list(SeptemberFloodExtent.objects.all())
            elif month == 'july':
                flood_extents = list(JulyFloodExtent.objects.all())
            elif month == 'august':
                flood_extents = list(AugustFloodExtent.objects.all())
            else:
                return JsonResponse({'error': 'Invalid month parameter'}, status=400)

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

            # Cache the fetched data for future requests
            cache.set(cache_key, geojson_data)

            return JsonResponse(geojson_data)

        else:
            return JsonResponse({'error': 'Month parameter is required'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def pakistan_admin_boundary(request):
    try:
        cache_key = 'pakistan_admin_boundary'  # Define a cache key

        # Attempt to fetch cached data first
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(cached_data)

        admin_boundaries = list(PakAdministrativeBoundary.objects.all())

        features = []
        for boundary in admin_boundaries:
            geom = GEOSGeometry(boundary.geom.wkt)
            features.append({
                "type": "Feature",
                "geometry": geom.geojson,
                "properties": {
                    "id": boundary.id,
                    # Add other properties here if needed
                }
            })

        geojson_data = {
            "type": "FeatureCollection",
            "features": features
        }

        # Cache the fetched data for future requests
        cache.set(cache_key, geojson_data)

        return JsonResponse(geojson_data)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def nha_road_network(request):
    try:
        cache_key = 'nha_road_network'

        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(cached_data)

        admin_boundaries = list(NHARoadNetwork.objects.all())

        features = []
        for boundary in admin_boundaries:
            geom = GEOSGeometry(boundary.geom.wkt)
            features.append({
                "type": "Feature",
                "geometry": geom.geojson,
                "properties": {
                    "id": boundary.id,
                    # Add other properties here if needed
                }
            })

        geojson_data = {
            "type": "FeatureCollection",
            "features": features
        }

        cache.set(cache_key, geojson_data)

        return JsonResponse(geojson_data)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def cache_and_response(cache_key, queryset):
    cached_data = cache.get(cache_key)
    if cached_data:
        return JsonResponse(cached_data)

    features = []
    for item in queryset:
        geom = GEOSGeometry(item.geom.wkt)  # Assuming geom is a PolygonField or PointField
        features.append({
            "type": "Feature",
            "geometry": geom.geojson,
            "properties": {
                "id": item.id,
                # Add other properties here if needed
            }
        })

    geojson_data = {
        "type": "FeatureCollection",
        "features": features
    }

    cache.set(cache_key, geojson_data)

    return JsonResponse(geojson_data)
  
def airport(request):
    try:
        if 'month' in request.GET:
            month = request.GET['month']
            if month == 'june':
                airports = JuneAirport.objects.all()
            elif month == 'july':
                airports = JulyAirport.objects.all()
            elif month == 'august':
                airports = AugustAirport.objects.all()
            elif month == 'september':
                airports = SeptemberAirport.objects.all()
            else:
                return JsonResponse({'error': 'Invalid month parameter'}, status=400)
        else:
            return JsonResponse({'error': 'Month parameter is required'}, status=400)

        cache_key = f'airport_{month}'
        return cache_and_response(cache_key, airports)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def health(request):
    try:
        if 'month' in request.GET:
            month = request.GET['month']
            if month == 'june':
                healths = JuneHealth.objects.all()
            elif month == 'july':
                healths = JulyHealth.objects.all()
            elif month == 'august':
                healths = AugustHealth.objects.all()
            elif month == 'september':
                healths = SeptemberHealth.objects.all()
            else:
                return JsonResponse({'error': 'Invalid month parameter'}, status=400)
        else:
            return JsonResponse({'error': 'Month parameter is required'}, status=400)

        cache_key = f'health_{month}'
        return cache_and_response(cache_key, healths)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def road(request):
    try:
        if 'month' in request.GET:
            month = request.GET['month']
            if month == 'june':
                roads = JuneRoads.objects.all()
            elif month == 'july':
                roads = JulyRoads.objects.all()
            elif month == 'august':
                roads = AugustRoads.objects.all()
            elif month == 'september':
                roads = SeptemberRoads.objects.all()
            else:
                return JsonResponse({'error': 'Invalid month parameter'}, status=400)
        else:
            return JsonResponse({'error': 'Month parameter is required'}, status=400)

        cache_key = f'road_{month}'
        return cache_and_response(cache_key, roads)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def settlement(request):
    try:
        if 'month' in request.GET:
            month = request.GET['month']
            if month == 'june':
                settlements = SettlementsJune.objects.all()
            elif month == 'july':
                settlements = SettlementsJuly.objects.all()
            elif month == 'august':
                settlements = SettlementsAug.objects.all()
            elif month == 'september':
                settlements = SettlementsSept.objects.all()
            else:
                return JsonResponse({'error': 'Invalid month parameter'}, status=400)
        else:
            return JsonResponse({'error': 'Month parameter is required'}, status=400)

        cache_key = f'settlement_{month}'
        return cache_and_response(cache_key, settlements)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def school(request):
    try:
        if 'month' in request.GET:
            month = request.GET['month']
            if month == 'june':
                schools = SchoolsJune.objects.all()
            elif month == 'july':
                schools = SchoolsJuly.objects.all()
            elif month == 'august':
                schools = SchoolsAug.objects.all()
            elif month == 'september':
                schools = SchoolsSept.objects.all()
            else:
                return JsonResponse({'error': 'Invalid month parameter'}, status=400)
        else:
            return JsonResponse({'error': 'Month parameter is required'}, status=400)

        cache_key = f'school_{month}'
        return cache_and_response(cache_key, schools)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
   
def map_view(request):
    return render(request, 'map.html')