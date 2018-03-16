from django.shortcuts import render
from third_app import form
# Create your views here.

def index(request):
    return render(request,'third_app/index.html')

def register(request):
    if request.method == 'POST':
        user_form = form.UserForm(request.POST)
        profile_form=form.UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

                profile.save()
    else:
        user_form = form.UserForm()
        profile_form = form.UserProfileForm()
        return render(request,'third_app/register.html',{user_form:'user_form',profile_form:'profile_form'})
