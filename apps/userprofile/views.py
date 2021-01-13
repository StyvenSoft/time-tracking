from django.contrib.auth from login
from django.contrib.auth import UserCreationForm
from django.contrib.auth import User
from django.shortcuts import render, redirect

# Import models

from .models import UserProfile

# Views

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()

            userprofile = Userprofile.objects.create(user=user)
            login(request, user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()
    
    return render(request, 'userprofile/signup.html', {'form':form})

