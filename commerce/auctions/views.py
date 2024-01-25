from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render 
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User , Category , Listing , Comment ,Bids

def index(request):
    # check if active or not
    active_listing=Listing.objects.filter(is_active=True)
    # the chow all our category in our  html
    allcategories= Category.objects.all()         
    # send the data in .html file
    return render(request, "auctions/index.html",{
        "listings": active_listing,
        "categories":allcategories,      
    } )
# Add bid
def add_bid(request, id):
    new_bid = request.POST["new_bid"]
    listing_data = Listing.objects.get(pk=id)
    
    listing_is_in_watchlist = request.user in listing_data.watch_list.all()  # I will check if watchlist in our user ,
    all_comments=Comment.objects.filter(listing=listing_data)
    
    isowner = request.user == listing_data.owner
    
    if int(new_bid) > listing_data.price.bid_amount:
        update_bid = Bids(user=request.user, bid_amount=int(new_bid))
        update_bid.save()
        
        listing_data.price = update_bid
        listing_data.save()
        
        return render(request, "auctions/listing.html", {
            "listing": listing_data,
            "message": "Bid is successful",
            "listing_is_in_watchlist":listing_is_in_watchlist,
            "all_comments":all_comments,
            "update": True,
            "isowner":isowner
        })   
    else:
        return render(request, "auctions/listing.html", {
            "listing": listing_data,
            "message": "Bid is unsuccessful",
            "listing_is_in_watchlist":listing_is_in_watchlist,
            "all_comments":all_comments,
            "update": False,
            "isowner":isowner
        })

    
# end def

# create a function add comment   
def add_comment(request, id):
    current_user = request.user
    listing_data = Listing.objects.get(pk=id)
    message = request.POST["new_comment"]
    
    new_comment = Comment(
        writer=current_user,
        listing=listing_data,
        message=message
    )
    
    new_comment.save()

    
    return HttpResponseRedirect(reverse("listing", args=(id,)))
# end def

# create a function that define listing
def listing(request, id):
    listing_data=Listing.objects.get(pk=id)
    listing_is_in_watchlist = request.user in listing_data.watch_list.all()  # I will check if watchlist in our user ,
    all_comments=Comment.objects.filter(listing=listing_data)
    isowner = request.user == listing_data.owner

    return render(request, "auctions/listing.html", {
        "listing":listing_data,
        "listing_is_in_watchlist":listing_is_in_watchlist,
        "all_comments":all_comments,
        "isowner":isowner,
        })   
# end def

def close_auction(request, id):
    listing_data=Listing.objects.get(pk=id)
    listing_data.is_active= False
    listing_data.save() 
    
    listing_is_in_watchlist = request.user in listing_data.watch_list.all()  # I will check if watchlist in our user ,
    all_comments=Comment.objects.filter(listing=listing_data)
    isowner = request.user == listing_data.owner


    return render(request, "auctions/listing.html", {
        "listing":listing_data,
        "listing_is_in_watchlist":listing_is_in_watchlist,
        "all_comments":all_comments,
        "isowner":isowner,
        "update": True,
        "message":"will then! Your action is closed",
        
        }) 
# end def

# I create fun that add in the watchlist
def add_watchlist(request, id):
    current_user=request.user
    listing_data=Listing.objects.get(pk=id)
    listing_data.watch_list.add(current_user)
    return HttpResponseRedirect(reverse("listing", args=(id,)))    
# end def

# I create fun that remove from the watchlist
def remove_watchlist(request, id):
    current_user=request.user
    listing_data=Listing.objects.get(pk=id)
    listing_data.watch_list.remove(current_user)
    return HttpResponseRedirect(reverse("listing", args=(id,)))  
# end def

# function to show/display my watchlist
def showwatchlist(request):
    current_user = request.user
    
    # Check if the user is authenticated
    if current_user.is_authenticated:
        # Access the userOFwatchlist attribute only if the user is authenticated
        listings = current_user.userOFwatchlist.all()
        return render(request, 'auctions/watchlist.html', {'listings': listings})
    else:
        # Handle the case when the user is not authenticated (AnonymousUser)
        return render(request, 'auctions/error.html', {'listings': []})
    
# end def

# function to show/display my categories
def schowcategory(request):
    # if 
    if request.method=="POST":
        categoryfromform=request.POST['category']
        category=Category.objects.get(nameOFcategory=categoryfromform)
        # check if active or not
        active_listing=Listing.objects.filter(is_active=True, category=category)
        # the chow all our category in our  html
        allcategories= Category.objects.all()         
        # send the data in .html file
        return render(request, "auctions/index.html",{
            "listings": active_listing,
            "categories":allcategories,      
        } )
# function 
    
# end def

# I create listing
def createListing(request):
    if request.method == "GET":
        allcategories = Category.objects.all()
        return render(request, "auctions/create.html", {"categories": allcategories})
    else:
        title = request.POST["title"]
        description = request.POST["description"]
        fotoURL = request.POST["fotoURL"]
        price_str = request.POST["price"]
        category_name = request.POST["category"]

        current_user = request.user

        try:
            # converting the price string to a float
            price = float(price_str)
        except ValueError:
            # Handle the case when the conversion fails , if price_str is not a valid float
            # show an error message to the user
            return render(request, "auctions/error.html", {"error_message": "Error"})

        # Create a new Bids object with the correct field name
        bid = Bids(bid_amount=price, user=current_user)
        bid.save()

        # Get the category using the name
        category_data = Category.objects.get(nameOFcategory=category_name)

        # Create a new listing with the bid object
        new_listing = Listing(
            title=title,
            description=description,
            fotoURL=fotoURL,
            price=bid,
            category=category_data,
            owner=current_user,
        )

        new_listing.save()

        return HttpResponseRedirect(reverse("index"))   
# end def

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
