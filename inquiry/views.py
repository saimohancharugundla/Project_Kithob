from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Inquiry
import requests
from django.conf import settings
# Create your views here.
url = "https://www.fast2sms.com/dev/bulk"

def inquiry(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        owner_email = request.POST['owner_mail']
        owner_id = request.POST['owner_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_inquired = Inquiry.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_inquired:
                messages.error(request,'You have already made an inquiry for this book')
                return redirect('/listings/'+listing_id+'/')
            inquiries = Inquiry(listing_id=listing_id,user_id=user_id,name=name,email=email,phone=phone,message=message,listing=listing,owner_id = owner_id)
            inquiries.save()
            send_mail(
                'Inquiry for your book '+listing,
                'You have an inquiry for '+listing+'. Check it out! \n',
                settings.EMAIL_HOST_USER,
                [owner_email],
                fail_silently=False
            )
            payload = "sender_id=FSTSMS&message=Someone is asking your product \n{} \n Check it out here! https://www.kithob.herokuapp.com/accounts/dashboard &language=english&route=p&numbers={}".format(listing,phone)
            headers = {
                'authorization': "jF6Lu0aGps4onb1HeQgqIzcwZB2t8AU3xE7kivNSVKDPymlYhOABH2E5yoct460SZJLhfqMrCFlOwIeQ",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
                }
            response = requests.request("POST", url, data=payload, headers=headers)
            messages.success(request,'Yay! Your Inquiry has been made. Owner may get back to you soon!')

            return redirect('/listings/'+listing_id+'/')


