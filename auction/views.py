from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


def start_page(request):
    auctions = Auction.objects.order_by('time_starting')
    pictures = Picture.objects.all()
    return render(request, 'auction/index.html', {'auctions': auctions, 'pictures': pictures})


def sign_up(request):
    if request.method == 'POST':
        logout(request)
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_again = form.cleaned_data['password_again']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.filter(username=username).first()
            if user is not None:
                form.add_error('username', 'User already exists!')
            elif password != password_again:
                form.add_error('password_again', 'Passwords mismatch!')
            else:
                user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name, last_name=last_name)
                Profile.objects.create(user=user, balance=0)
                login(request, user)
                return redirect(reverse('edit_user'))
    else:
        form = SignupForm()
    return render(request, 'auction/signup.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        logout(request)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('start_page'))
            else:
                form.add_error(None, 'Invalid credentials!')
    else:
        form = LoginForm()
    return render(request, 'auction/signin.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect(reverse('start_page'))


def add_auction(request):
    if request.method == 'POST':
        form = AddAuctionForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['image']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            min_price = form.cleaned_data['min_price']
            bid_rate = form.cleaned_data['bid_rate']
            time_ending = form.cleaned_data['time_ending']
            seller = request.user
            picture = Picture.objects.create(image=img, title=title, description=description, category=category,
                                             user_id=seller.id)
            Auction.objects.create(picture_id=picture.id, seller_id=seller.id, buyer_id=seller.id, time_ending=time_ending,
                                   current_price=min_price, bid_rate=bid_rate, lifecycle='Active')
            return redirect(reverse('start_page'))
    else:
        form = AddAuctionForm()
    return render(request, 'auction/add_auction.html', {'form': form})


def watch_auction(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)
    if request.method == 'POST':
        form = WatchAuctionForm(request.POST)
        if form.is_valid():
            new_price = form.cleaned_data['new_price']
            buyer = request.user
            bid_rate = auction.bid_rate
            current_price = auction.current_price
            if buyer.is_authenticated:
                if new_price >= current_price + bid_rate:
                    auction.current_price = new_price
                    auction.buyer = buyer
                    auction.save()
                    return HttpResponseRedirect(reverse('auction_by_id', kwargs={'auction_id': auction_id}))
                else:
                    form.add_error(None, f'Minimum rate should be {current_price + bid_rate}!')
            else:
                form.add_error(None, f'Please log in or sign up!')
    else:
        form = WatchAuctionForm()
    return render(request, 'auction/watch_auction.html', {'form': form, 'auction': auction, })


def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile = Profile.objects.get(user=user)
    return render(request, 'auction/profile.html', {'user': user, 'profile': profile})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = EditProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('user_by_id', kwargs={'user_id': request.user.id}))
        return render(request,
                      'auction/edit_profile.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)
        return render(request,
                      'auction/edit_profile.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})