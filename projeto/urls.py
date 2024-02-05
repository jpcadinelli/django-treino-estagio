from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home')

def sobre(request):
    return HttpResponse('Sobre')

def contato(request):
    return HttpResponse('Contato')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home), # Home
    path('sobre/', sobre), # /sobre/
    path('contato/', contato), # /contato/
]
