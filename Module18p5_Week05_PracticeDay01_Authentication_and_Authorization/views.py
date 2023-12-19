from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def submission(request):
    return render(request, 'submission.html')
