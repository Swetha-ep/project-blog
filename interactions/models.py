from django.db import models
from django.contrib.auth.models import User
from home.models import Posts
from django.utils import timezone
# Create your models here.

class Subscription(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE,related_name='subscriptions')
    subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE,related_name='subscribers')

    def __str__(self):
        return f'{self.subscriber.username} subscribed {self.subscribed_to.username}'
    

class Saved(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='saved_posts')
    posts = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='savers')
    saved_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} saved {self.posts.title}'
    

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='liked_by')
    u_posts = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='liked')
    liked_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} liked {self.u_posts.title}'