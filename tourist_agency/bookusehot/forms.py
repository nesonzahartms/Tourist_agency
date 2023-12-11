from django import forms
from .models import Review, Booking, Person
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


# Форма поиска отелей
class HotelSearchForm(forms.Form):
    name = forms.CharField(required=False)
    country = forms.CharField(required=False)
    category = forms.IntegerField(required=False)
    options = forms.CharField(required=False)


# Форма создания отзыва
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']


#
#
# Форма для входа
class AgencyLoginForm(AuthenticationForm):
    pass


#
#
# # Форма для регистрации
class AgencyRegistrationForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ['name', 'password1', 'password2']


#
#
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date']
