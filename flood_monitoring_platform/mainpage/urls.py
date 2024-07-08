from django.urls import path
from . import views

urlpatterns = [
    path('flood_extent/', views.flood_extent, name='flood_extent'),
    path('pakistan_admin_boundary/', views.pakistan_admin_boundary, name='pakistan_admin_boundary'),
    path('airport/', views.airport, name='airport'),
    path('nha_road_network/', views.nha_road_network, name='nha_road_network'),
    path('health/', views.health, name='health'),
    path('road/', views.road, name='road'),
    path('settlement/', views.settlement, name='settlement'),
    path('school/', views.school, name='school'),
    path('', views.map_view, name='map_view'),
]
