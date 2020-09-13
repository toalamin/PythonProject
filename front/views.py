from django.http import HttpResponse
from django.shortcuts import render
from .models import Aboutus
from .models import Slider
from .models import Client



def index(request):
    aboutData = Aboutus.objects.all()[0]
    sliderData = Slider.objects.all()
    clientData = Client.objects.all()
    context = {
        'about': aboutData,
        'slide': sliderData,
        'clientInfo': clientData,
    }
    return render(request,'index.html',context)


def portfolio(request):
    return render(request,'front/portfolio.html')
    
    
def price(request):
    return render(request,'front/price.html') 


def blog(request):
    return render(request,'front/blog.html')    


def about(request):
    return render(request,'front/about.html')