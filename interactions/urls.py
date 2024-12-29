from django.urls import path
from .views import *

urlpatterns = [
    path('subscribe/<int:pk>/',subscribe,name='actions-subscribe'),
    path('unsubscribe/<int:pk>/',unsubscribe,name='actions-unsubscribe'),
    path('subscribers/',subscribers,name='user-subscriptions'),
    path('toggle-save/<int:pk>/',toggle_save_post,name='actions-save'),
    path('saved/',saved_posts,name='actions-saved-posts'),
    path('toggle_upvote_post/<int:pk>/',toggle_upvote_post,name='actions-upvote'),
]