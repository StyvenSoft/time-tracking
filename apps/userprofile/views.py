from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Import models

from .models import Userprofile

# Views

@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()

        messages.info(request, 'The change was saved')

        return redirect('myaccount')
    
    return render(request, 'userprofile/edit_profile.html')

