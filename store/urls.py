from django.urls import path
from . import views

urlpatterns = [
     path('', views.p,name='p'),
     path('', views.c,name='c'),
     path('', views.j,name='j'),
     path('', views.ruby,name='ruby'),
     path('', views.cplus,name='cplus'),
     path('', views.csharp,name='csharp'),
     path('', views.php,name='php'),
     path('', views.electrical,name='electrical'),
     path('', views.civil,name='civil'),
     path('', views.electronics,name='electronics'),

]
  