from django.urls import path
from . import views

urlpatterns = [
    path('flood_extent/',views.flood_extent, name='flood_extent'),
    path('',views.map_view,name='map_view'),
]