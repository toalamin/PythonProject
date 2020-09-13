from django.http import HttpResponse
from django.shortcuts import render

def about(Request):
    text = {
        "name" : "Al Amin",
        "email" : "toalaminbd@gmail.com",
        "phone" : '01918887654',
        "friendList" : ['AlAmin','Jamal','Kamal','Rasel','Kalam','Mamun']
    }
    return render(Request,'about.html',text)
    
def contact(Request):
    return render(Request,'contact.html')
    
    
def home(Request):
    return render(Request,'index.html')

