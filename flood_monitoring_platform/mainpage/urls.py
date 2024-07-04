from django.urls import path
from . import views
from .views import flood_extent_view

urlpatterns = [
    path('flood_extent/',views.flood_extent_view, name='flood_extent'),
    path('',views.map_view,name='map_view'),
]