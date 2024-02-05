from django.contrib import admin
from django.urls import path

def my_view():
    ...

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', my_view)
]
