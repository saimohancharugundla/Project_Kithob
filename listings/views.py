from django.shortcuts import render,redirect,get_object_or_404
from .models import Listing
from django.core.paginator import Paginator,EmptyPage
# Create your views here.

def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator= Paginator(listings,8)
    page_num = request.GET.get('page')
    page_listings = paginator.get_page(page_num)
    context = {
        'listings':page_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request,pk):
    listing = get_object_or_404(Listing,pk=pk)
    context = {
        'listing' : listing
    }
    return render(request,'listings/listing.html',context)

def search(request):
    query_set = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set = query_set.filter(description__icontains=keywords)
    context = {
        'query_set':query_set
    }
    return render(request,'listings/search.html',context)
def CSETEXTBOOKS(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='CSE',sub_category='TB')
    paginator= Paginator(listings,9)
    page_num = request.GET.get('page')
    page_listings = paginator.get_page(page_num)
    context = {
        'cse_textbooks':page_listings
    }
    return render(request,'listings/cse_tb.html',context)

def CSENOTEBOOKS(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='CSE',sub_category='NB')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'cse_notebooks':page_listings
    }
    return render(request,'listings/cse_nb.html',context)

def CSECM(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='CSE',sub_category='CM')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'cse_cm':page_listings
    }
    return render(request,'listings/cse_complete.html',context)

def ECETEXTBOOKS(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='ECE',sub_category='TB')
    paginator= Paginator(listings,9)
    page_num = request.GET.get('page')
    page_listings = paginator.get_page(page_num)
    context = {
        'ece_textbooks':page_listings
    }
    return render(request,'listings/ece_tb.html',context)

def ECENOTEBOOKS(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='ECE',sub_category='NB')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'ece_notebooks':page_listings
    }
    return render(request,'listings/ece_nb.html',context)

def ECECOMPLETE(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='ECE',sub_category='CM')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'ece_complete':page_listings
    }
    return render(request,'listings/ece_complete.html',context)

def CIVILNOTEBOOKS(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='CIVIL',sub_category='NB')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'civil_notebooks':page_listings
    }
    return render(request,'listings/civil_nb.html',context)

def CIVILTEXTBOOKS(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='CIVIL',sub_category='TB')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'civil_textbooks':page_listings
    }
    return render(request,'listings/civil_tb.html',context)

def CIVILCOMPLETE(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='CIVIL',sub_category='CM')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'civil_complete':page_listings
    }
    return render(request,'listings/civil_complete.html',context)

def MECHTEXTBOOKS(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='MECH',sub_category='TB')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'mech_textbooks':page_listings
    }
    return render(request,'listings/mech_tb.html',context)

def MECHNOTEBOOKS(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='MECH',sub_category='NB')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'mech_notebooks':page_listings
    }
    return render(request,'listings/mech_nb.html',context)

def MECHCOMPLETE(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='MECH',sub_category='CM')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'mech_complete':page_listings
    }
    return render(request,'listings/mech_complete.html',context)

def CHEMICALTEXTBOOKS(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='CHE',sub_category='TB')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'chemical_textbooks':page_listings
    }
    return render(request,'listings/chemical_tb.html',context)

def CHEMICALNOTEBOOKS(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='CHE',sub_category='NB')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'chemical_notebooks':page_listings
    }
    return render(request,'listings/chemical_nb.html',context)


def CHEMICALCOMPLETE(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='CHE',sub_category='CM')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'chemical_complete':page_listings
    }
    return render(request,'listings/chemical_complete.html',context)


def MMETEXTBOOKS(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='MME',sub_category='TB')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'mme_textbooks':page_listings
    }
    return render(request,'listings/mme_tb.html',context)

def MMENOTEBOOKS(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='MME',sub_category='NB')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'mme_notebooks':page_listings
    }
    return render(request,'listings/mme_nb.html',context)


def MMECOMPLETE(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True,category='MME',sub_category='CM')
    paginator= Paginator(listings,9)
    pagenum = request.GET.get('page')
    page_listings = paginator.get_page(pagenum)
    context = {
        'mme_complete':page_listings
    }
    return render(request,'listings/mme_complete.html',context)