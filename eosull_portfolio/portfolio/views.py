from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello There, this is the first step to building your portfolio site")