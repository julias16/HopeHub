from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def clothsfirst(request):
    return render(request, 'clothsfirst.html')
def contactus(request):
    return render(request, 'contactus.html')
def furniturefirst(request):
    return render(request, 'furniturefirst.html')
def foodfirst(request):
    return render(request, 'foodfirst.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
def donateform(request):
    return render(request, 'donateform.html')
def blog(request):
    return render(request, 'blog.html')
def faq(request):
    return render(request, 'faq.html')
def privacypolicy(request):
    return render(request, 'privacypolicy.html')
def termsconditions(request):
    return render(request, 'termsconditions.html')
def messagethanks(request):
    return render(request, 'messagethanks.html')