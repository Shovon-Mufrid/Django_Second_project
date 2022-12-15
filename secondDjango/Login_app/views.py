from django.shortcuts import render
from Login_app.forms import UserForm, UserInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from Login_app.models import UserInfo
# from Login_app import form

# Create your views here.

def index(request):
    dict={}
    # video 9.8 start
    if request.user.is_authenticated:
        current_user = request.user # person that is logged in 
        # print(current_user.username) #print in console
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = UserInfo.objects.get(user__pk=user_id) #user is for oneToOne relation in models // __ is specified columns> model user & user's id >>> it will be occure the one that is called from a model and other one should have a field of that model
        
        dict={'user_basic_info': user_basic_info, 'user_more_info': user_more_info}  
    # end video

    return render(request, 'Login_app/index.html', context=dict)



def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST) #data variable for future task
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save() #save in user model
            user.set_password(user.password) #encrypted password
            user.save()

            # user info form
            user_info = user_info_form.save(commit=False) #it won't go to database now 
            user_info.user = user #one to one relation from model.py , this connect user and user info
            
            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic'] #not necessary to write this, alrady in models.py

            user_info.save() #commit=true // not part of second if condition
           
            registered = True   #registration done  

    else:  #this will load first when registered is false
        user_form = UserForm()
        user_info_form = UserInfoForm()

    dict = {'user_form': user_form, 'user_info_form': user_info_form, 'registered': registered}
    return render(request, 'Login_app/register.html', context = dict)


def login_page(request):
    dict= {}
    return render(request, 'Login_app/login.html', context=dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username') #get information from  form by the username as username(form name)
        password = request.POST.get('password')

        user = authenticate(username = username, password = password) # 2nd username is variable, 1st username is object of function from user table to match

        if user:                        # authenticate true by default
            if user.is_active:        # active true by default
                login(request, user)    # it will pass user value to log in
                return HttpResponseRedirect(reverse('Login_app:index'))

            else: #inactive account
                return HttpResponse("Account Is Not Active")        


        else: #if credintial are wrong
             return HttpResponse("Login Details are wrong")


    else: # if calling user_login in url without form submitting page: login_html
        # return render(request, 'Login_app/login.html', context={}) 
          return HttpResponseRedirect(reverse('Login_app:login'))        


@login_required     # decorators called in top if requirement satisfied
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_app:index'))





