from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User ,Post ,Follow,Like
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


def index(request):
    # get all posts
    all_posts = Post.objects.all().order_by('id').reverse()
    # Pagination
    paginator = Paginator(all_posts, 5) # Show 5 posts per page.
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    # check  all Likes
    all_likes = Like.objects.all()
    
    likes_by_user = []
    try:
        for like in all_likes:
            if like.user.id == request.user.id :
                likes_by_user.append(like.post.id)
    except:
        likes_by_user= []

    # Render the index template with the paginated posts
    return render(request, "network/index.html", {
        'all_posts': all_posts,
        'page_obj': page_obj,
        'likes_by_user': likes_by_user,
        })
       
# create the add like
@csrf_exempt
def add_liked(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=request.user.id)
    newLike = Like(user=user, post=post)
    newLike.save()
    return JsonResponse({"message": "Like added!"})

# create the remove liked
@csrf_exempt
def remove_liked(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=request.user.id)
    like = Like.objects.filter(user=user, post=post)
    like.delete()
    return JsonResponse({"message": "Like removed!"})

# create a new function edit
@csrf_exempt
def edit(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        data = json.loads(request.body)
        content = data.get('content')
        if content:
            post.content = content
            post.save()
            return JsonResponse({'status': 'success', 'content': post.content})
        else:
            return JsonResponse({'status': 'error', 'message': 'Content cannot be empty'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
#create function for new POST 
def new_post(request):
    if request.method == 'POST':
        content = request.POST["content"]
        user = User.objects.get(pk=request.user.id)
        post = Post( content=content, user=user)
        post.save()
        return HttpResponseRedirect(reverse("index"))

# create a new function for profile
def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    posts = Post.objects.filter(user=user).order_by('-date')

    # Following and followers this profile
    following = Follow.objects.filter(userFollower=user)
    followers = Follow.objects.filter(userFollowing=user)

    # Check if the current user is following the profile user
    if request.user.is_authenticated:
        is_following = Follow.objects.filter(userFollower=request.user, userFollowing=user).exists()
    else:
        is_following = False

    # Pagination
    paginator = Paginator(posts, 10)  # Show 10 posts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/profile.html", {
        'page_obj': page_obj,
        'username': user.username,
        'posts': posts,
        'following': following,
        'followers': followers,
        'is_following': is_following,
        'user_p': user,
    })

#  create a new function following 
def following(request):
    current_user = request.user
    following_people = Follow.objects.filter(userFollower=current_user)
    all_posts = Post.objects.all().order_by('-id')  # Order by descending id

    following_posts = []

    for post in all_posts:
        for person in following_people:
            if person.userFollowing == post.user:
                following_posts.append(post)

    # Pagination
    paginator = Paginator(following_posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Render the index template with the paginated posts
    return render(request, "network/following.html", {
        'page_obj': page_obj,
    })
    
# create a function Follow
def follow(request):
    userfollow = request.POST['userfollow']
    current_User = User.objects.get(pk=request.user.id)
    follow_id_data = User.objects.get(username=userfollow)
    foll = Follow(userFollower=current_User, userFollowing=follow_id_data)
    foll.save()
    
    user_id = follow_id_data.id
    return HttpResponseRedirect(reverse("profile", kwargs={"user_id": user_id }))

# create a function Unfollow
def unfollow(request, user_id):
    userfollow = request.POST['userfollow']
    current_User = User.objects.get(pk=request.user.id)
    follow_id_data = User.objects.get(username=userfollow)
    foll = Follow.objects.get(userFollower=current_User, userFollowing=follow_id_data)
    foll.delete()
    
    return HttpResponseRedirect(reverse("profile", kwargs={"user_id": user_id }))


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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
