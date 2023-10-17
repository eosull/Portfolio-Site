from django.shortcuts import render


def home(request):
    # View returning index page
    return render(request, 'home/index.html')