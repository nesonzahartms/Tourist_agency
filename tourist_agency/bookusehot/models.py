from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


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
    name = models.CharField(max_length=100)


class Review(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.person.username + " - "


# class Person(AbstractUser):
#     USER_TYPE_CHOICES = (
#         (1, 'CUSTOMER'),
#         (2, 'AGENT'),
#     )
#     user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
#     pass

class Booking(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()


# class AgencyPerson(AbstractUser):
#     pass
# # Create your models here.
