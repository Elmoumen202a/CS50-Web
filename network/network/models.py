from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Post(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.id} made by {self.user} on {self.date.strftime('%Y-%m-%d %H:%M:%S')}"

class Follow(models.Model):
    userFollower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_follower', default=1)
    userFollowing = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_following', default=1)

    def __str__(self):
        return f"{self.userFollower} is following {self.userFollowing}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like') 
     
    def __str__(self):
        return f"{self.user} liked post {self.post}"