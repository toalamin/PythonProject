from django.contrib import admin

# Register your models here.
from .models import Aboutus
from .models import Slider
from .models import Client

admin.site.register(Aboutus)
admin.site.register(Slider)
admin.site.register(Client)
