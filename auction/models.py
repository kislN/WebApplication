from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    # balance = models.DecimalField(max_digits=6, decimal_places=2)
    cellphone = models.CharField(max_length=14)
    country = models.CharField(max_length=45)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='media/users/%Y/%m/%d', blank=True)

    def __str__(self):
        user = User.objects.get(id=self.user)
        return "id=" + str(self.pk) + " username=" + user.username + " email=" + user.email


class Picture(models.Model):
    CATEGORIES = (
                   ('LAND', 'Landscape'),
                   ('PORT', 'Portrait'),
                )
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/pictures/%Y/%m/%d', blank=True,
                              default='media/pictures/None/no-img.jpg')
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=100, choices=CATEGORIES)
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "ID:" + str(self.pk) + " " + self.title

class Auction(models.Model):
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.SET("(deleted)"), blank=True, null=True,
                              related_name="auction_winner", related_query_name="auction_winner")
    time_starting = models.DateTimeField(auto_now_add=True, blank=True)
    time_ending = models.DateTimeField()
    current_price = models.FloatField()
    bid_rate = models.IntegerField()

    LIFECYCLES_ = (
        ('A', 'Active'),
        ('B', 'Banned'),
        ('D', 'Due'),
        ('X', 'Adjudicated'),
    )
    lifecycle = models.CharField(max_length=100, choices=LIFECYCLES_)

    def __str__(self):
        return "ID:" + str(self.pk) + " PRODUCT_ID:" + str(self.picture)


# class Watchlist(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "USER_ID:" + str(self.user_id) + " AUCTION_ID:" + str(self.auction_id)
#
#
# class Bid(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
#     bid_time = models.DateTimeField()
#
#     def __str__(self):
#         return "USER_ID:" + str(self.user_id) + " AUCTION_ID:" + \
#                str(self.auction_id) + " " + str(self.bid_time)
#
#
# class Chat(models.Model):
#     auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     time_sent = models.DateTimeField()
#
#     def __str__(self):
#         return "AUCTION_ID:" + str(self.auction_id) + " USER_ID:" + str(self.user_id)

