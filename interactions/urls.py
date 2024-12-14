from django.urls import path
from .views import *

urlpatterns = [
    path('subscribe/<int:pk>/',subscribe,name='actions-subscribe'),
    path('unsubscribe/<int:pk>/',unsubscribe,name='actions-unsubscribe'),
    path('subscribers/',subscribers,name='user-subscriptions'),
]