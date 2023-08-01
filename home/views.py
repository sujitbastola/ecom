import pickle
from django.conf import settings
from django.http import HttpResponse
from .models import *
from .forms import *
import re
import uuid
from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.hashers import make_password,check_password
from django.core.mail import send_mail
from django.contrib import messages
from django.db.models import Q
import random
from django.utils.text import slugify
from django.core.paginator import Paginator
from c_admin.models import *

from django.db.models import Prefetch



# Create your views here.

#nav bar components
def home(request):
    category=Category.objects.all()
    context = {'category': category}
    return render(request, "home/index.html",context)

def about(request):
    return render(request, "home/about.html")
def offers(request):
    return render(request, "home/offers.html")
def special(request):
    return render(request, "home/special.html")
def order(request):
    return render(request, "home/order.html")

#Detail components
def detail(request):
    return render(request, "home/detail.html")

def cetegories_detail(request,cat_slug):
    category=Category.objects.get(slug=cat_slug)
    product=Product.objects.filter(category__slug= cat_slug).prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.all())
        )

    context = {'category': category,'product':product}
    return render(request, "home/cetegories_detail.html",context)



# authentication

def Login(request,):
    users = Users.objects.all()
    if request.method=="POST":
        emails= request.POST['email_address']
        password= request.POST['passwords']
        users = Users.objects.filter (Q(email__iexact=emails))
        remember = request.POST.get('rememberme', '')
        
        for user in users:
            if emails in user.email:
                if password:
                    if check_password(password,user.password):
                        if user.is_email_verified==True:
                            if remember=="1":
                                user_dict = {
                                'id': user.id,
                                'first_name':user.first_name,
                                'last_name':user.last_name,
                                'email':user.email,
                                'password':user.password,
                                'is_email_verified': user.is_email_verified,
                                }
                                request.session['is_authenticated'] = user_dict
                            else:
                                user_dict = {
                                'id': user.id,
                                'first_name':user.first_name,
                                'last_name':user.last_name,
                                'email':user.email,
                                'is_email_verified': user.is_email_verified,
                                }
                                request.session['is_authenticated'] = user_dict
                            return redirect('home')
                        else: 
                            return HttpResponse("Email is not verified")
                    else:
                        return HttpResponse("Invalid password")
                else:
                    return HttpResponse("Enter Password")
            else:
                return HttpResponse("Invalid email")

    return render(request,'auth/login.html')



def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+\[\]{};:\'"\\|,.<>\/?]).{8,}$'
    return re.match(pattern, password) is not None

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def Signup(request):
    if request.method == "POST":
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email_address')
        passwords = request.POST.get('passwords')
        cpassword = request.POST.get('c_password')

        if fname:
            if lname:
                if email:
                    if validate_email(email):
                        user = Users.objects.filter(email=email).first()
                        if not user:
                            if passwords:
                                if validate_password(passwords):
                                    if passwords == cpassword:
                                        hashed_password = make_password(passwords)
                                        # Generate verification token
                                        uid = uuid.uuid4()
                                        user = Users(first_name=fname, last_name=lname, email=email, password=hashed_password, token=uid)
                                        user.save()
                                        send_mail(
                                            subject="Verify your account",
                                            message='Click on the link below to verify your account. http://127.0.0.1:8000/authentication/{}'.format(uid),
                                            from_email=settings.EMAIL_HOST_USER,
                                            recipient_list=[user.email],
                                            fail_silently=False
                                        )
                                        return HttpResponse('Account created successfully! Check your email and click on the link to verify.', status=200)
                                    else:
                                        return HttpResponse('Passwords do not match', status=400)
                                else:
                                    return HttpResponse('Password must contain at least 1 number, 1 capital letter, and 1 special character', status=400)
                            else:
                                return HttpResponse('Password is required', status=400)
                        else:
                            return HttpResponse('Email is already taken', status=400)
                    else:
                        return HttpResponse('Invalid email address', status=400)
                else:
                    return HttpResponse('Email address is required', status=400)
            else:
                return HttpResponse('Last name is required', status=400)
        else:
            return HttpResponse('First name is required', status=400)
    
    return render(request, 'auth/register.html')


# #! verify email

def account_verify(request, token):
    users = Users.objects.filter(token=token).first()
    users.is_email_verified = True  
    users.save() 
    return redirect('login')



# def logout(request):
#     if 'is_authenticated' in request.session:
#         del request.session['is_authenticated']
#     return redirect('home')

def logout(request):
    auth_logout(request)  # Call the logout function from Django's authentication system
    return redirect('home')

def profile(request):
    return render(request,'account/profile.html')

def buynow(request):
    return render(request,'actions/buynow.html')

def addtolist(request):
    return render(request,'actions/mylist.html')


def upload_image(request):
    if request.method == "POST":

        image = request.FILES.get("image")
        name = request.POST["name"]
        coustumeorder = CustomDesignedorder(image=image, name=name)
        coustumeorder.save()
        return redirect('home')
    return render(request,'home/order.html')




  