from django.urls import path
from .import views
urlpatterns = [
    path('login/', views.loginpage,name='login.page'), 
    path('registration/', views.registration,name='registration.page'), 
    path('forgotpassword/', views.forgotpassword,name='forgot.page'), 
    path('logout/', views.signout,name='logout'), 
]