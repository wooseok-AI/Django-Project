from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World.")

def some_url(request):
    return HttpResponse("Added Some URL")