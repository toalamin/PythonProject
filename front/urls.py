
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index,name="home"),
    path('portfolio/', views.portfolio,name='portfolio.page'),
    path('price/', views.price,name='price.page'),
    path('blog/', views.blog,name='blog.page'),
    path('about/', views.about,name='about.page'),
    
]