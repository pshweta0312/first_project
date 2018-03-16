from django.urls import path
from sec_app.views import index,user,form_detail_view


urlpatterns = [
    path('index/',index,name='index'),
    path('users/',user,name = 'user'),
    path ('form-details/',form_detail_view,name='form-details')

]