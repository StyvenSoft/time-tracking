# Import functionality from django

from django.shortcuts import render

# Views

def frontpage(request):
    return render(request, 'core/frontpage.html')
