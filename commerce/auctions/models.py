from django.contrib.auth.models import AbstractUser
from django.db import models

# creat listing category
class User(AbstractUser):
    pass

class Category(models.Model):
    nameOFcategory= models.CharField(max_length=60)
    
    #SHOW NAMES OF CATEGORIES
    def __str__(self) -> str:
        return self.nameOFcategory
# create a class Bids

#class Bids(models.Model):
#    bid=models.FloatField(default=0)
#   user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,  related_name="user_bids")
    
#    def __str__(self) :
#        return self.bid

class Bids(models.Model):
    bid_amount = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_bids")

    def __str__(self):
        return f'{self.bid_amount}'
    
    

class Listing(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=500)
    fotoURL = models.CharField(max_length=2000)
    price = models.ForeignKey(Bids, on_delete=models.CASCADE, blank=True, null=True, related_name="price_bids")
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    watch_list = models.ManyToManyField(User, blank=True, related_name="userOFwatchlist")

    # show names of titles
    def __str__(self) -> str:
        return self.title

# create a class for comment
class  Comment(models.Model):
    writer=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,  related_name="user_comment")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listing_comment")
    message=models.CharField(max_length=500)
        
    def __str__(self) -> str:
        return  f"{self.writer} comment on {self.listing}"
        
