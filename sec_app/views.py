from django.shortcuts import render
from sec_app.models import User
from sec_app.myform import FormDetails


# Create your views here.
def index(request):
    return render(request,'sec_app/index.html')
def user(request):
    userlist =User.objects.order_by('first_name')
    mydict = {'user_list': userlist}
    return render(request,'sec_app/show_users.html',context=mydict)

def form_detail_view(request):
    form =FormDetails()

    if request.method == 'POST':

        form = FormDetails(request.POST)
        if form.is_valid():

            print(form.cleaned_data['first_name'])
            print(form.cleaned_data['last_name'])
            print(form.cleaned_data['email_id'])

    return render(request,'sec_app/from_details.html',{'form':form})
