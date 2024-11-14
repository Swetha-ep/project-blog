from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created successfully. You can login now.')
            return redirect('login')
        else:
            messages.error(request, "There was an error in your registration form.")
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


def custom_logout(request):
    logout(request)
    return render(request, 'users/logout.html')


@login_required
def profile(request):
    return render(request,'users/profile.html')