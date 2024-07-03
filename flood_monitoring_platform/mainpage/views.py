from django.http import HttpResponse, HttpResponseServerError
from django.db import connection
import math
import gzip
import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)

def get_mvt(request, z, x, y):
    try:
        # Define the bounds of the tile
        tile_bounds = tile_to_bounds(x, y, z)

        # SQL Query
        sql = """
            SELECT ST_AsMVT(mvtgeom.*, 'flood_extent') FROM (
                SELECT
                    ST_AsMVTGeom(
                        ST_Transform(geom, 3857),
                        ST_Transform(ST_SetSRID(ST_MakeEnvelope(%s, %s, %s, %s), 4326), 3857),
                        4096,
                        64,
                        true
                    ) AS geom,
                    id
                FROM flood.flood_aug
                WHERE ST_Intersects(geom, ST_SetSRID(ST_MakeEnvelope(%s, %s, %s, %s), 4326))
            ) AS mvtgeom;
        """

        with connection.cursor() as cursor:
            cursor.execute(sql, [tile_bounds[0], tile_bounds[1], tile_bounds[2], tile_bounds[3],
                                 tile_bounds[0], tile_bounds[1], tile_bounds[2], tile_bounds[3]])
            tile = cursor.fetchone()[0]

            # Gzip compression
            compressed_tile = gzip.compress(tile)

            response = HttpResponse(compressed_tile, content_type="application/x-protobuf")
            response['Content-Encoding'] = 'gzip'
            
            logger.info(f"MVT tile generated successfully for z={z}, x={x}, y={y}")
            return response
    except Exception as e:
        logger.error(f"Error generating MVT tile for z={z}, x={x}, y={y}: {str(e)}")
        return HttpResponseServerError("Error generating MVT tile")

def tile_to_bounds(x, y, z):
    n = 2.0 ** z
    lon_left = x / n * 360.0 - 180.0
    lat_bottom = 180.0 / math.pi * math.atan(math.sinh(math.pi * (1 - 2 * y / n)))
    lon_right = (x + 1) / n * 360.0 - 180.0
    lat_top = 180.0 / math.pi * math.atan(math.sinh(math.pi * (1 - 2 * (y + 1) / n)))
    return (lon_left, lat_bottom, lon_right, lat_top)

def map_view(request):
    return render(request, 'mainpage/map.html')
