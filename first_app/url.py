from django.urls import path
from first_app import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('home/',views.home,name ='home'),
    path('static-img/',views.img,name='image'),
]