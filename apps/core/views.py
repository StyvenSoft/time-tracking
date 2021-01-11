# Import functionality from django

from django.shortcuts import render

# Views

def frontpage(request):
    return render(request, 'core/frontpage.html')

def privacy(request):
    return render(request, 'core/privacy.html')

def plans(request):
    return render(request, 'core/plans.html')
