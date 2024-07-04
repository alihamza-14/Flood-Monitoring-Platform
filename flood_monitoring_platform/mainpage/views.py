from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import June, July, August, September
from django.contrib.gis.geos import GEOSException

def flood_extent_view(request):
    month = request.GET.get('month')
    try:
        if month == 'june':
            flood_extents = get_list_or_404(June)
        elif month == 'july':
            flood_extents = get_list_or_404(July)
        elif month == 'aug':
            flood_extents = get_list_or_404(August)
        elif month == 'sep':
            flood_extents = get_list_or_404(September)
        else:
            return JsonResponse({'error': 'Invalid month'}, status=400)
        
        data = serialize('geojson', flood_extents)
        return JsonResponse(data, safe=False)
    
    except GEOSException as e:
        return JsonResponse({'error': f'GEOS error: {str(e)}'}, status=500)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def map_view(request): 
    return render(request, 'map.html')
