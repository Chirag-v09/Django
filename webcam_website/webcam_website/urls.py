from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.livefe, name="livefe"),
    path('admin/', admin.site.urls),
]