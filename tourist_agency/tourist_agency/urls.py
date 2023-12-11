from django.contrib import admin
from django.urls import path, include
from bookusehot import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('index/', views.get_index),
    path('user/', views.get_person),
    path('find_hotel/', views.find_hotel),
    path('get_login/', views.get_login, name='login'),
    path('get_hotel_gallery/', views.get_hotel_gallery, name='logout'),
    path('create_review/', views.create_review),
    path('get_agency_login/', views.get_agency_login),
    path('get_agency_registration/', views.get_agency_registration),
    path('booking_hotel/', views.booking_hotel),
    path('get_homepage/', views.booking_hotel),
]