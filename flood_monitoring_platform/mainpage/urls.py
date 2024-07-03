from django.urls import path
from . import views

urlpatterns = [
    path('flood_extent/july/', views.flood_extent_july, name='flood_extent_july'),
    path('flood_extent/june/', views.flood_extent_june, name='flood_extent_june'),
    path('flood_extent/august/', views.flood_extent_august, name='flood_extent_august'),
    path('', views.map_view, name='map_view'),
]
