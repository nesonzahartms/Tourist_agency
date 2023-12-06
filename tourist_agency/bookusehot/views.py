from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


# @login_required
def make_reservation(request):  # Обработка формы бронирования
    return render(request, 'reservation.html')
