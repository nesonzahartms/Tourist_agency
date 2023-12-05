from django.shortcuts import render, redirect
from .models import Hotel, HotelImage, Agency, Category, Country
from .forms import HotelSearchForm, ReviewForm, AgencyLoginForm, AgencyRegistrationForm, BookingForm
from django.contrib.auth import login
from django.views.generic import ListView, DetailView


def hotel_search(request):  # Обработка запроса поиска отелей
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


def hotel_gallery(request, hotel_id):  # Обработка запроса изображений отеля
    hotel = Hotel.objects.get(id=hotel_id)
    images = HotelImage.objects.filter(hotel=hotel)

    return render(request, 'hotel_gallery.html', {'hotel': hotel, 'images': images})


def create_review(request, agency_id):  # Обработка запроса отзывов
    agency = Agency.objects.get(id=agency_id)

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


def agency_login(request):  # Представление для входа
    if request.method == 'POST':
        form = AgencyLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Перенаправьте на страницу после успешной аутентификации
    else:
        form = AgencyLoginForm()

    return render(request, 'agency_login.html', {'form': form})


def agency_registration(request):  # Представление для регистрации
    if request.method == 'POST':
        form = AgencyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Перенаправлениее на страницу после успешной регистрации
    else:
        form = AgencyRegistrationForm()

    return render(request, 'agency_registration.html', {'form': form})


def hotel_booking(request, hotel_id): # Представление для бронирования
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


def homepage(request):
    categories = Category.objects.all()
    countries = Country.objects.all()
    hotels = Hotel.objects.all()

    context = {
        'categories': categories,
        'countries': countries,
        'hotels': hotels,
    }

    return render(request, 'homepage.html', context)



# class HotelListView(ListView):
#     model = Hotel
#     template_name = 'hotels/hotel_list.html'
#
#
# class HotelDetailView(DetailView):
#     model = Hotel
#     template_name = 'hotels/reservation.html'
# # Create your views here.
