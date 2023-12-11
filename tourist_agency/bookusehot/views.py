from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .forms import HotelSearchForm, ReviewForm, AgencyLoginForm, AgencyRegistrationForm, BookingForm
from .models import Hotel, Country, Category, HotelImage, Person


def get_index(request):
    return render(request, 'index.html')


def get_person(request):
    return render(request, 'login.html')


def find_hotel(request):  # Обработка запроса поиска отелей
    form = HotelSearchForm(request.GET)
    hotels = Hotel.objects.all()

    if form.is_valid():
        name = form.cleaned_data.get('name')
        country = form.cleaned_data.get('country')
        category = form.cleaned_data.get('category')

        if name:
            hotels = hotels.filter(name__icontains=name)
        if country:
            hotels = hotels.filter(country__icontains=country)
        if category:
            hotels = hotels.filter(category=category)

        return render(request, 'hotel_search.html', {'form': form, 'hotels': hotels})
    else:
        form = HotelSearchForm()

    return render(request, 'hotel_search.html', {'form': form})


def get_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    person = authenticate(request, username=username, password=password)
    if person is not None:
        login(request, person)
        return redirect('home')
    else:
        return render(request, 'auth/login.html', {'error': 'Invalid username or password'})
#


def get_hotel_gallery(request, hotel_id):  # Обработка запроса изображений отеля
    hotel = Hotel.objects.get(id=hotel_id)
    images = HotelImage.objects.filter(hotel=hotel)

    return render(request, 'hotel_gallery.html', {'hotel': hotel, 'images': images})


def create_review(request, agency_id):  # Обработка запроса отзывов
    agency = Person.objects.get(id=agency_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.agency = agency
            review.save()
            return redirect('agency_detail', agency_id=agency_id)
    else:
        form = ReviewForm()

    return render(request, 'create_review.html', {'form': form, 'agency': agency})


def get_agency_login(request):  # Представление для входа
    if request.method == 'POST':
        form = AgencyLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Перенаправьте на страницу после успешной аутентификации
    else:
        form = AgencyLoginForm()

    return render(request, 'agency_login.html', {'form': form})


def get_agency_registration(request):  # Представление для регистрации
    if request.method == 'POST':
        form = AgencyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Перенаправлениее на страницу после успешной регистрации
    else:
        form = AgencyRegistrationForm()

    return render(request, 'agency_registration.html', {'form': form})


def booking_hotel(request, hotel_id): # Представление для бронирования
    hotel = Hotel.objects.get(id=hotel_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.hotel = hotel
            booking.save()
            return redirect('booking_confirmation')  # Перенаправление на страницу подтверждения бронирования
    else:
        form = BookingForm()

    return render(request, 'hotel_booking.html', {'form': form, 'hotel': hotel})


def get_homepage(request):
    categories = Category.objects.all()
    countries = Country.objects.all()
    hotels = Hotel.objects.all()

    context = {
        'categories': categories,
        'countries': countries,
        'hotels': hotels,
    }

    return render(request, 'homepage.html', context)
