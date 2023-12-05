from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Hotel(models.Model):
    objects = ()
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    options = models.ManyToManyField('Option', blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class HotelImage(models.Model):
    objects = ()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotel_images/')

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def __str__(self):
        return self.hotel.name + " - " + str(self.id)


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Отзывы
class Agency:

    def __str__(self):
        return self


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.user.username + " - " + self.agency.name


class AgencyUser(AbstractUser):
    pass


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return self.user.username + " - " + self.hotel.name
