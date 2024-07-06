from django.urls import path
from . import views

urlpatterns = [
    path('flood_extent/july/', views.flood_extent_july, name='flood_extent_july'),
    path('flood_extent/june/', views.flood_extent_june, name='flood_extent_june'),
    path('flood_extent/august/', views.flood_extent_august, name='flood_extent_august'),
    path('settlements_aug/', views.settlements_aug, name='settlements_aug'),
    path('settlements_june/', views.settlements_june, name='settlements_june'),
    path('settlements_july/', views.settlements_july, name='settlements_july'),
    path('settlements_sept/', views.settlements_sept, name='settlements_sept'),
    path('airport_june/', views.airport_june, name='airport_june'),
    path('airport_july/', views.airport_july, name='airport_july'),
    path('airport_aug/', views.airport_aug, name='airport_aug'),
    path('airport_sept/', views.airport_sept, name='airport_sept'),
    path('pak/', views.pak, name='pak'),
    path('health_june/', views.health_june, name='health_june'),
    path('health_july/', views.health_july, name='health_july'),
    path('health_aug/', views.health_aug, name='health_aug'),
    path('health_sept/', views.health_sept, name='health_sept'),
    path('school_june/', views.school_june, name='school_june'),
    path('school_july/', views.school_july, name='school_july'),
    path('school_aug/', views.school_aug, name='school_aug'),
    path('school_sept/', views.school_sept, name='school_sept'),
    path('nharoads/', views.nharoads, name='nharoads'),
     
    path('', views.map_view, name='map_view'),
]
