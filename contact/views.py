from django.shortcuts import render
from django.http import HttpResponse
from .models import Contactus

# Create your views here.


def contact(request):
    if request.method == 'POST':
       name = request.POST.get('name')
       email = request.POST.get('email')
       subject = request.POST.get('subject')
       message = request.POST.get('message')
       contactData = Contactus(name=name,email=email,subject=subject,message=message)
       contactData.save()
    return render(request,'front/contact.html')