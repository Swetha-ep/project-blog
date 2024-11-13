from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account is created {username}!')
            return redirect('home-index')
        else:
            messages.error(request, "There was an error in your registration form.")
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})