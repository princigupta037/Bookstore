from django.urls import path
from . import views 
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    # book categories url
    url('admin/', admin.site.urls),
    path('booklist/',views.book_list, name='book_list'),
    path('register/' , views.reg, name='reg'),
    path('login/', views.log, name='log'),
    # book list urls
    path('c',views.c, name='c'),
    path('m',views.m,name='m'),
    path('e',views.e,name='e'),
    path('el',views.el,name='el'),
    path('ci',views.ci,name='ci'),
    
    # book data urls
    path('civ/<int:pk>/',views.civ,name='cv_list'),
    path('elecro/<int:pk>/',views.electro,name='e_list'),
    path('elec/<int:pk>/',views.elec,name='el_list'),
    path('mech/<int:pk>/',views.mech,name='m_list'),
    path('comp/<int:pk>/',views.comp, name='c_list'),
]
  