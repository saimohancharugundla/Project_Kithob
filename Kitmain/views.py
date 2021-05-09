from django.shortcuts import render,redirect
from listings.views import listings
from listings.models import Listing
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    context = {
        'listings':listings
    }
    return render(request,'Kitmain/home_index.html',context)

def products(request):
    return render(request,'Kitmain/product_index.html')

@login_required
def sell(request):
    if request.method == 'POST':
        bookname = request.POST.get('bookTitle')
        bookcategory = request.POST.get('bookCategory')
        bookType = request.POST.get('bookType')
        bookdescription = request.POST.get('bookDescription')
        bookprice = request.POST.get('bookPrice')
        img_main = request.FILES['imgmain']
        img_ref1 = request.FILES['imgref1']
        img_ref2 = request.FILES['imgref2']
        img_ref3 = request.FILES['imgref3']
        img_ref4 = request.FILES['imgref4']
        print("bookname",bookname)
        add_books = Listing.objects.create(title = bookname,category = bookcategory,sub_category = bookType,description=bookdescription,price=bookprice,photo_main=img_main,photo_1=img_ref1,photo_2=img_ref2,photo_3=img_ref3,photo_4=img_ref4,owner=request.user)
        add_books.save()
        return redirect('/')
    else:
        return render(request,'Kitmain/sell.html')
    