from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return HttpResponse("this is aboutpage")
def services(request):
    return HttpResponse("this is our services page")
def Contact(request):
    return HttpResponse("this is our Contact page")