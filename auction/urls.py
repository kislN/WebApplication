from django.urls import path
from .views import *

urlpatterns = [
    path('', start_page, name='start_page'),
    path('signin/', log_in, name='signin'),
    path('signup/', sign_up, name='signup'),
    path('signout/', log_out, name='signout'),
    path('addauction/', add_auction, name='addauction'),
    path('<int:auction_id>/', watch_auction, name='auction_by_id'),
    path('user/<int:user_id>/', profile, name='user_by_id'),
    path('user/edit/', edit_profile, name='edit_user'),
    # path('register/', register_page, name='register_page'),
    # path('register/new_user/', register, name='register'),
    # path('category/<str:category>/', filter_auctions, name='filter_auctions'),
    # path('watchlist/<int:auction_id>/', watchlist, name='watchlist'),
    # path('balance/', balance, name='balance'),
    # path('balance/topup/', topup, name='topup'),
    # path('watchlist/', watchlist_page, name='watchlist'),
    # path('bid/<int:auction_id>/', bid_page, name='bid_page'),
    # path('bid/<int:auction_id>/comment/', views.comment, name='comment'),
    # path('bid/<int:auction_id>/raise_bid/', views.raise_bid, name='raise_bid'),

]
