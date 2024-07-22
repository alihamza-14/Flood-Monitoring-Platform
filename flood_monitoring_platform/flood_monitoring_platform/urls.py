from django.contrib import admin
from django.urls import path,include
# from mainpage import views
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]