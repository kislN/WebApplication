from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    cellphone = models.CharField(max_length=14)
    country = models.CharField(max_length=45)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='media/users/%Y/%m/%d', blank=True)

    def __str__(self):
        user = User.objects.get(id=self.user_id)
        return "id=" + str(self.pk) + " username=" + user.username + " email=" + user.email

    def get_absolute_url(self):
        return reverse('user_by_id', kwargs={'user_id': self.user_id})


class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
        return self.title
        # return "ID:" + str(self.pk) + " " + self.title


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

    def get_absolute_url(self):
        return reverse('auction_by_id', kwargs={'auction_id': self.id})



