from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from .models import *
from home.models import Posts
from users.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
# Create your views here.

@login_required
def subscribe(request,pk):
    subscribed_to=get_object_or_404(User,id=pk)
    Subscription.objects.get_or_create(subscriber=request.user,subscribed_to=subscribed_to)
    messages.success(request,"Thank you for subscribing")
    return render(request,'home/about.html')

@login_required
def unsubscribe(request,pk):
    subscribed_to=get_object_or_404(User,id=pk)
    subscription=Subscription.objects.filter(subscriber=request.user,subscribed_to=subscribed_to)
    subscription.delete()
    messages.info(request,"You have unsubscribed this user")
    return render(request,'home/about.html')

@login_required
def subscribers(request):
    subs = Subscription.objects.filter(subscriber=request.user).values_list('subscribed_to',flat=True)
    profile= Profile.objects.filter(user__in=subs)
    print(profile)
    context={
        'profile' : profile
    }
    return render(request,'interactions/subscribers.html',context)

@login_required
def toggle_save_post(request,pk):
    post = get_object_or_404(Posts,id=pk)
    saved_post = Saved.objects.filter(user=request.user,posts=post)
    if saved_post.exists():
        saved_post.delete()
        messages.success(request,'Post have been removed from saved successfully.')
    else:
        Saved.objects.create(user=request.user,posts=post)
        messages.success(request,'Post has been saved successfully.')  
    return redirect ('/')

@login_required
def saved_posts(request):
    saved_posts = Saved.objects.filter(user=request.user).select_related('posts').order_by('-saved_date')
    upvoted_posts = Like.objects.filter(user=request.user).values_list('u_posts',flat=True)
    posts_with_likes = Posts.objects.annotate(total_likes=Count('liked'))
    for saved in saved_posts:
        post = saved.posts
        post.is_liked = post.id in upvoted_posts
        post.total_likes=posts_with_likes.get(id=post.id).total_likes
    paginator = Paginator(saved_posts,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={
        'page_obj': page_obj
        }
    return render(request,'interactions/saved.html',context)


@login_required
def toggle_upvote_post(request,pk):
    post = get_object_or_404(Posts,id=pk)
    upvote_post = Like.objects.filter(user=request.user,u_posts=post)
    if upvote_post.exists():
        upvote_post.delete()
        messages.success(request,'Upvote has been removed from this post.')
    else:
        Like.objects.create(user=request.user,u_posts=post)
        messages.success(request,'An upvote is given to this post successfully.')
    return redirect ('/')