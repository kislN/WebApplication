from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.db.models import *


class ProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    list_display = ('user', 'cellphone', 'country', 'date_of_birth')
    ordering = ('user',)
    list_filter = ('country', )
    view_on_site = True


class PictureAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    list_display = ('title', 'category', 'date_posted')
    ordering = ('-date_posted',)
    list_display_links = ('title',)
    readonly_fields = ('date_posted',)
    view_on_site = True


class AuctionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    list_display = ('id', 'picture', 'seller', 'buyer', 'current_price',
                    'bid_rate', 'time_starting', 'time_ending', 'lifecycle')
    ordering = ('time_starting',)
    list_filter = ('lifecycle', 'seller', 'buyer')
    list_editable = ('lifecycle',)
    readonly_fields = ('time_starting', )
    view_on_site = True


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Auction, AuctionAdmin)


