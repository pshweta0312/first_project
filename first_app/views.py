from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    my_disc={'insert_me':'inserted from view','second_key':'again from view'}
    return render(request,'first_app/index.html',my_disc)



def home(request):
    return HttpResponse("WELCOME TO HOME PAGE")
def img(request):
    return render(request,'first_app/static_image.html')