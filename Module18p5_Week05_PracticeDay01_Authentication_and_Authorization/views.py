from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required
def submission(request):
    return render(request, 'submission.html')
