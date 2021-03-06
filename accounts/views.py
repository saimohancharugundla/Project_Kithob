from django.shortcuts import render,redirect
from Kitcore.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
import random
import string
from listings.models import Listing
from inquiry.models import Inquiry
import re
# Create your views here.

def randomString(stringlength=6):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringlength))

code = randomString()

def register(request):
    
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        user = User
        context = {
            'first_name':fname,
            'last_name':lname,
            'username':uname,
            'email':email,
            'phone':phone,
            'password':password,
        }
        regex = r'^(O16[0-9][0-9][0-9]+[@][rguktong.ac.in]|o16[0-9][0-9][0-9]+[@][rguktong.ac.in])'
        if re.search(regex,email):
            if password == cpassword:
                if user.objects.filter(username = uname).exists():
                    messages.error(request,'Username already taken')
                    return redirect('register')
                else:
                    if user.objects.filter(email = email).exists():
                        messages.error(request,'Email already exists')
                        return redirect('register')
                    else:
                        if user.objects.filter(phone = phone).exists():
                            messages.error(request,'Phone Number already exists')
                            return redirect('register')
                        else:
                            send_mail(
                                'Account Creation Confirmation!',
                                'Hi '+fname +', Your Confirmation Code is: '+code,
                                'saimohancharugundla@gmail.com',
                                [email],
                                fail_silently = False
                                )
                            request.method='GET'
                            return render(request,'accounts/confirmregister.html',context)
            else:
                messages.error(request,'Password do not matched!')
                return redirect('register')
        else:
            messages.error(request,'Email format is not correct! Kindly use your University Email Id')
            return redirect('register')
                
    else:
        return render(request,'accounts/register.html')

def confirmregister(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirmcode = request.POST['confirmcode']
        user = User
        context = {
            'first_name':fname,
            'last_name':lname,
            'username':uname,
            'email':email,
            'phone':phone,
            'password':password,
        }
        if code == confirmcode:
            user = user.objects.create_user(username=uname,email=email,first_name=fname,last_name=lname,phone=phone,password=password)
            user.save()
            login(request,user)
            messages.success(request,'You are logged in as '+uname)
            return redirect('home')
        else:
            messages.error(request,'Invalid Confirmation Code')
            return render(request,'accounts/confirmregister.html',context)
    else:
        return redirect('register')

def signin(request):
    if request.method == 'POST':
        uname = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(username = uname,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Welcome back '+uname)
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')


@login_required
def signout(request):
	logout(request)
	return redirect('/')


@login_required
def dashboard(request):
    mylistings = Listing.objects.order_by('-list_date').filter(owner=request.user)
    myinquiry = Inquiry.objects.all().filter(user_id=request.user.id)
    myinquiries_count = Inquiry.objects.all().filter(user_id=request.user.id).count()
    mylistings_count = Listing.objects.all().filter(owner=request.user).count()
    inquiries_received = Inquiry.objects.all().filter(owner_id = request.user.id)
    inquiries_received_count = Inquiry.objects.all().filter(owner_id = request.user.id).count()
    print("My Inquiries\n")
    print(myinquiry)
    print(mylistings)
    #receiverd_inquiries = Inquiry.objects.all().filter(owner_id=request.user.id)
    context = {
        'listingss' : mylistings,
        'inquiries': myinquiry,
        'myinq_count' : myinquiries_count,
        'mylist_count' : mylistings_count,
        'inq_received' : inquiries_received,
        'inq_received_count' : inquiries_received_count,
        #'receiverd_inquiries':receiverd_inquiries
    }
    return render(request,'accounts/profile.html',context)
