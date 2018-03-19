from django.urls import path
from sec_app import views

app_name = 'sec_app'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('users/',views.user,name = 'user'),
    path ('form-details/',views.form_detail_view,name='form-details'),
    path('relative/',views.relative,name = 'relative'),
    path('home/',views.home,name = 'home')
]