from django.urls import path
from . import views
from .views import get_mvt

urlpatterns = [
    path('get_mvt/<str:layer>/<int:z>/<int:x>/<int:y>/', views.get_mvt, name='get_mvt'),
    # path('flood_extent/',views.flood_extent, name='flood_extent'),
    path('',views.map_view,name='map_view'),
]