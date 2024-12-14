from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Subscription(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE,related_name='subscriptions')
    subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE,related_name='subscribers')

    def __str__(self):
        return f'{self.subscriber.username} subscribed {self.subscribed_to.username}'