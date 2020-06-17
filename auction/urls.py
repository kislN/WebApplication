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

]
