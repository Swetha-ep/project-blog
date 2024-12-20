from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='home-index'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'), 
    path('user/<str:username>/',UserPostListView.as_view(),name='user-posts'),
    path('about/', about, name='home-about'),
    path('search/',search,name='search'),
    path('subscribed_blogs/',SubscribedPostListView.as_view(),name='user-subscribers-posts'),
]
