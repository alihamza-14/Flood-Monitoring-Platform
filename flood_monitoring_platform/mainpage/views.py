from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import JuneFloodExtent, SeptemberFloodExtent, JulyFloodExtent, AugustFloodExtent, PakAdministrativeBoundary, JuneAirport, JulyAirport, AugustAirport, SeptemberAirport, NHARoadNetwork
from django.contrib.gis.geos import GEOSGeometry

def flood_extent(request):
    try:
        if 'month' in request.GET:
            month = request.GET['month']
            if month == 'june':
                flood_extents = JuneFloodExtent.objects.all()
            elif month == 'september':
                flood_extents = SeptemberFloodExtent.objects.all()
            elif month == 'july':
                flood_extents = JulyFloodExtent.objects.all()
            elif month == 'august':
                flood_extents = AugustFloodExtent.objects.all()
            else:
                return JsonResponse({'error': 'Invalid month parameter'}, status=400)
        else:
            return JsonResponse({'error': 'Month parameter is required'}, status=400)

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
        return JsonResponse({'error': str(e)}, status=500)

def pakistan_admin_boundary(request):
    try:
        admin_boundaries = PakAdministrativeBoundary.objects.all()
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
        return JsonResponse(geojson_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)



def nha_road_network(request):
    try:
        admin_boundaries = NHARoadNetwork.objects.all()
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
        return JsonResponse(geojson_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


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

        features = []
        for airport in airports:
            geom = GEOSGeometry(airport.geom.wkt)  # Assuming geom is a PolygonField or PointField
            features.append({
                "type": "Feature",
                "geometry": geom.geojson,
                "properties": {
                    "id": airport.id,
                    # Add other properties here if needed
                }
            })

        geojson_data = {
            "type": "FeatureCollection",
            "features": features
        }
        return JsonResponse(geojson_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def map_view(request):
    return render(request, 'map.html')