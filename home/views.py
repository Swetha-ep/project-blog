from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Posts
# Create your views here.


def index(request):
    context={
    'posts' : Posts.objects.all()
    }
    return render(request,'home/index.html',context)


def about(request):
    return render(request,'home/about.html',{'title': 'About'})
