from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import Subscription
from home.models import Posts
from users.models import Profile
from django.contrib import messages
from django.db.models import Subquery,OuterRef
# Create your views here.

def subscribe(request,pk):
    subscribed_to=get_object_or_404(User,id=pk)
    Subscription.objects.get_or_create(subscriber=request.user,subscribed_to=subscribed_to)
    messages.success(request,"Thank you for subscribing")
    return render(request,'home/about.html')

def unsubscribe(request,pk):
    subscribed_to=get_object_or_404(User,id=pk)
    subscription=Subscription.objects.filter(subscriber=request.user,subscribed_to=subscribed_to)
    subscription.delete()
    messages.info(request,"You have unsubscribed this user")
    return render(request,'home/about.html')

def subscribers(request):
    subs = Subscription.objects.filter(subscriber=request.user).values_list('subscribed_to',flat=True)
    profile= Profile.objects.filter(user__in=subs)
    print(profile)
    context={
        'profile' : profile
    }
    return render(request,'interactions/subscribers.html',context)