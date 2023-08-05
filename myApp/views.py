from django.db import IntegrityError
from django.shortcuts import render,redirect

from django.http import JsonResponse,HttpRequest

from django.contrib.auth.models import User

from .models import *

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

# Create your views here.


def login_view (request):

    return render (request,'log.html')


def sign_up_view(request):

    return render(request,'signup.html')



def create_user(request):

    if request.method=='POST':

        uname = request.POST['username']
        mob = request.POST['mobile']
        em = request.POST['email']
        pword = request.POST['password']

        try:

            user= User.objects.create(username=uname,email=em,password=pword)

            user.set_password(pword)

            user.save()

            user_mobile = UserMobile.objects.create(user=user,mobile=mob)

            user_mobile.save()

            return redirect('login_view')
        
        except IntegrityError:

            return render(request,'signup.html',{'message':'User Already Exist..!','uname':uname,'mob':mob,'email':em,'password':pword})



def user_login(request):

    if request.method=='POST':

        user_name = request.POST['username']

        pword = request.POST['password']

        user = authenticate(request,username=user_name,password=pword)

        if user is not None:

            request.session['id']=user_name

            

            login(request,user)

            return redirect('home')
        
        else:

            return render(request,'log.html',{'message':'Invalid username or Password..!'})
        


def log_out(request):

    logout(request)

    return redirect('login_view')
        

@login_required
def home_view(request):

    data = to_do_list.objects.filter(user_name=request.session['id'])

    return render(request,'home.html',{'todo':data})



def check_login(request):

    if request.user.is_authenticated:

        return redirect('home')
    
    else:

        return redirect('login_view')
    


def add_todo_list(request):

    if request.method=='POST':

        u = request.session['id']

        t = request.POST.get('title')

        d = request.POST.get('description')

        data = to_do_list.objects.create(user_name=u,title=t,description=d)

        data.save()

        return JsonResponse({'success':'success'},safe=False)
    

    else:

        return JsonResponse({'error':'not post request'})
    


def delete_individual(request,id):

    print(id)

    data = to_do_list.objects.get(id=id)

    data.delete()

    get_data = to_do_list.objects.filter(user_name=request.session['id'])

    return render(request,'home.html',{'todo':get_data})



def edit_each(request):

    if request.method=='POST':

        getTitle = request.POST.get('title')

        print(getTitle)

        getDesc = request.POST.get('desc')

        get_id = request.POST.get('id')


        to_do_list.objects.filter(id=get_id).update(title=getTitle,description=getDesc)
        
        return JsonResponse ({'success':'success'},safe=False)