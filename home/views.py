from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

posts=[
 {
    'title' : 'blog1',
    'author' : 'a1',
    'content' : 'aaaaaa',
    'date_posted' : datetime(2024,11,1)
  },
 {
    'title' : 'blog2',
    'author':'a2',
    'content' : 'bbbb',
    'date_posted' : datetime(2024, 10, 4)
}
 ]


def index(request):
    context={
    'posts' : posts
    }
    return render(request,'home/index.html',context)


def about(request):
    return render(request,'home/about.html',{'title': 'About'})
