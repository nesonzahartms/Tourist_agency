from django.contrib import admin
from django.urls import path, include
from bookusehot import views


urlpatterns = [
    path("admin", admin.site.urls),
    path('index', views.index),
    path('make_reservation', views.make_reservation),
]