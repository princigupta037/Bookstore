from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminlogin,name='adminlogin'),
    path('', views.newlogin,name='newlogin'),
    path('', views.catlog,name='catlog'),
]
   