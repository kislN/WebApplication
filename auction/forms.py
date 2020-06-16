from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        # fields = ('date_of_birth', 'photo')
        fields = ('cellphone',)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', max_length=1024, widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    email = forms.EmailField(label='E-Mail', max_length=256)
    first_name = forms.CharField(label='First name', max_length=56)
    last_name = forms.CharField(label='Last name', max_length=45)
    password = forms.CharField(label='Password', max_length=1024, min_length=3, widget=forms.PasswordInput)
    password_again = forms.CharField(label='Repeat password', max_length=1024, min_length=3, widget=forms.PasswordInput)


class AddAuctionForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField(label='Title', max_length=150)
    description = forms.CharField(label='Description', max_length=500, widget=forms.Textarea())
    CATEGORIES = (
        ('LAND', 'Landscape'),
        ('PORT', 'Portrait'),
    )
    category = forms.ChoiceField(choices=CATEGORIES)
    min_price = forms.FloatField()
    bid_rate = forms.IntegerField()
    time_ending = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M']) #, help_text="(Day/Month/Year Hour:Min)")



class WatchAuctionForm(forms.Form):
    new_price = forms.FloatField()

class TopUpForm(forms.Form):
    amount = forms.DecimalField(max_digits=6, decimal_places=2)

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)

# class confAuction(forms.Form):
#     CHOICES = [(x, x) for x in ("Yes", "No")]
#     option = forms.ChoiceField(choices=CHOICES)
#     title = forms.CharField(widget=forms.HiddenInput())
#
#
# class UserCreateForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")
#
#     def save(self, commit=True):
#         user = super(UserCreateForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user