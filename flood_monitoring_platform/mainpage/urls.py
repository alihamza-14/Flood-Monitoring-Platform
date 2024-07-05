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
    path('', views.map_view, name='map_view'),
]
