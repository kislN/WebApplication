from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.db.models import Max, F
from .models import *
from django.db.models import *

# Register your models here.


# class PostInline(admin.TabularInline):
#     def has_add_permission(self, request, obj):
#         return False
# #
#     model = Post
#     fields = ('subject', 'text', 'created_at', 'is_modified')
#     readonly_fields = ('subject', 'text', 'created_at', 'is_modified')
#     ordering = ('-created_at',)
#     show_change_link = True

#
# class PostAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return False
#
#     def get_queryset(self, request):
#         return super().get_queryset(request).annotate(author=F('blog__author__username'))
#
#     def author(self, obj):
#         return obj.author
#     author.admin_order_field = 'author'
#
#     list_display = ('author', 'subject', 'created_at', 'is_modified')
#     ordering = ('-created_at',)
#     list_display_links = ('subject',)
#     fields = ('blog', 'subject', 'text', 'created_at', 'updated_at')
#     readonly_fields = ('blog', 'created_at', 'updated_at')
#
#
class AuctionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
# #
#     def get_queryset(self, request):
#         return super().get_queryset(request).annotate(updated_at=Max('post__updated_at'))
# #
#     def updated_at(self, obj):
#         return obj.updated_at
#     updated_at.admin_order_field = 'updated_at'
# #
    list_display = ('seller', 'buyer')
#
#     ordering = ('title',)
#     fields = ('author', 'title', 'created_at')
#     readonly_fields = ('created_at',)
#     view_on_site = True
#     inlines = (PostInline,)
#
#
# admin.site.register(Blog, BlogAdmin)
# admin.site.register(Post, PostAdmin)

admin.site.register(Profile)
admin.site.register(Picture)
admin.site.register(Auction, AuctionAdmin)
# admin.site.register(Chat)
# admin.site.register(Watchlist)
# admin.site.register(Bid)


