from django.urls import path
from . import views

urlpatterns = [
    path('flood_extent/', views.flood_extent, name='flood_extent'),
    path('pakistan_admin_boundary/', views.pakistan_admin_boundary, name='pakistan_admin_boundary'),
    path('airport/', views.airport, name='airport'),
    path('', views.map_view, name='map_view'),
]
