from django.urls import path
from third_app import views

urlpatterns =[
    path('',views.index,name ='index'),
    path ('register/',views.register,name='register')
]