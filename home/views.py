from django.shortcuts import render,get_object_or_404
from .models import Posts
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.


class PostListView(ListView):
    model = Posts
    template_name = 'home/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


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
    


def about(request):
    return render(request,'home/about.html',{'title': 'About'})
