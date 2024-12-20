from django.shortcuts import render,get_object_or_404,redirect
from .models import Posts
from users.models import Profile
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator
from interactions.models import Subscription,Saved
# Create your views here.


class PostListView(ListView):
    model = Posts
    template_name = 'home/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        user=self.request.user
        if user.is_authenticated:
            saved_posts=Saved.objects.filter(user=user).values_list('posts',flat=True)
            for post in context['posts']:
                post.is_saved = post.id in saved_posts
        return context


class SubscribedPostListView(ListView):
    model = Posts
    template_name = 'home/subscribed_page.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3
    def get_queryset(self):
        subscribers=Subscription.objects.filter(subscriber=self.request.user).values_list('subscribed_to',flat=True)
        # return Posts.objects.filter(author__in=subscribers).order_by('-date_posted')
        return super().get_queryset().filter(author__in=subscribers)


class PostDetailView(DetailView):
    model = Posts


class PostCreateView(LoginRequiredMixin, CreateView):
    model=Posts
    fields=['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Posts
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class UserPostListView(ListView):
    model = Posts
    template_name = 'home/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Posts.objects.filter(author = user).order_by('-date_posted')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username= self.kwargs.get('username'))
        context['user_profile']=get_object_or_404(Profile,user=user)
        context['is_subscribed']=Subscription.objects.filter(
            subscriber=self.request.user,subscribed_to=user
        ).exists()
        return context


def about(request):
    return render(request,'home/about.html',{'title': 'About'})


def search(request):
    item = request.GET.get('q')
    if item:
        posts = Posts.objects.filter(
            Q(title__contains=item) |
            Q(author__username__contains=item)
            )
        
        if posts:
            print(posts)
        for post in posts:
            post.title = mark_safe(post.title.replace(item, f"<span style='background-color:yellow;'>{item}</span>"))
            post.author.username_highlighted = mark_safe(post.author.username.replace(item, f"<span style='background-color:yellow;'>{item}</span>"))
        if not posts:
            messages.error(request,"No results found.")
            return redirect('home-index')
    else:
        messages.error(request,"Please enter a search term")
        return redirect('home-index')
   
    # paginator = Paginator(posts, 3)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context={
        'posts' : posts,
        # 'page_obj': page_obj,
        # 'is_paginated': page_obj.has_other_pages(),
        # 'query': item
        }
    return render(request,'home/search.html',context)

