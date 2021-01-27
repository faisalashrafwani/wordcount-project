
from django.urls import path
from .import views

urlpatterns = [
    path('', views.intro),
    path('profile/', views.myprofile, name='goprofile'),
    path('homepage/', views.homepage, name='gohome'),
    path('count/', views.count, name='gocount'),

]
