from django.core import paginator
from . models import Product
from django.shortcuts import render,get_object_or_404
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator
from taggit.models import Tag
from django.db.models import Q

def Product_ListView(request,tag_slug=None):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    product_list=Product.objects.filter(
        Q(product_name__icontains=q) |
        Q(company1__icontains=q) |
        Q(company2__icontains=q) |
        Q(company3__icontains=q) |
        Q(company4__icontains=q) |
        Q(name1__icontains=q) |
        Q(name2__icontains=q) |
        Q(name3__icontains=q) |
        Q(name4__icontains=q)
    )
    products_count = product_list.count()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        product_list=product_list.filter(tags__in=[tag])
    paginator=Paginator(product_list,4)
    page_number=request.GET.get('page')
    try:
        product_list=paginator.page(page_number)
    except PageNotAnInteger:
        product_list=paginator.page(1)
    except EmptyPage:
        product_list=paginator.page(paginator.num_pages)        
    return render(request,'testapp/home.html',{'product_list':product_list,'tag':tag,'products_count':products_count})

def Pelectronic_view(request,tag_slug=None):
    product_list=Product.objects.filter(product1__icontains='electronics')
    products_count = product_list.count()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        product_list=product_list.filter(tags__in=[tag]) 
    paginator=Paginator(product_list,4)
    page_number=request.GET.get('page')
    try:
        product_list=paginator.page(page_number)
    except PageNotAnInteger:
        product_list=paginator.page(1)
    except EmptyPage:
        product_list=paginator.page(paginator.num_pages) 
    return render(request,'testapp/electronics.html',{'product_list':product_list,'products_count':products_count})

def Pfashion_view(request,tag_slug=None):
    product_list=Product.objects.filter(product1__icontains='fashion')
    products_count = product_list.count()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        product_list=product_list.filter(tags__in=[tag]) 
    paginator=Paginator(product_list,4)
    page_number=request.GET.get('page')
    try:
        product_list=paginator.page(page_number)
    except PageNotAnInteger:
        product_list=paginator.page(1)
    except EmptyPage:
        product_list=paginator.page(paginator.num_pages) 
    return render(request,'testapp/fashion.html',{'product_list':product_list,'products_count':products_count})  

def Pother_view(request,tag_slug=None):
    product_list=Product.objects.filter(product1__icontains='others')
    products_count = product_list.count()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        product_list=product_list.filter(tags__in=[tag]) 
    paginator=Paginator(product_list,4)
    page_number=request.GET.get('page')
    try:
        product_list=paginator.page(page_number)
    except PageNotAnInteger:
        product_list=paginator.page(1)
    except EmptyPage:
        product_list=paginator.page(paginator.num_pages) 
    return render(request,'testapp/others.html',{'product_list':product_list,'products_count':products_count})     

def Psports_view(request,tag_slug=None):
    product_list=Product.objects.filter(product1__icontains='sports')
    products_count = product_list.count()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        product_list=product_list.filter(tags__in=[tag]) 
    paginator=Paginator(product_list,4)
    page_number=request.GET.get('page')
    try:
        product_list=paginator.page(page_number)
    except PageNotAnInteger:
        product_list=paginator.page(1)
    except EmptyPage:
        product_list=paginator.page(paginator.num_pages) 
    return render(request,'testapp/sports.html',{'product_list':product_list,'products_count':products_count})        


from django.shortcuts import render,get_object_or_404
from . models import Trends
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator
from taggit.models import Tag

# Create your views here.
def news_view(request,tag_slug=None):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    trends_list=Trends.objects.filter(
        Q(title__icontains=q) |
        Q(source__icontains=q)
    )
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        trends_list=trends_list.filter(tags__in=[tag])
    paginator=Paginator(trends_list,4)
    page_number=request.GET.get('page')
    try:
        trends_list=paginator.page(page_number)
    except PageNotAnInteger:
        trends_list=paginator.page(1)
    except EmptyPage:
        trends_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/news.html',{'trends_list':trends_list,'tag':tag})

def news_national(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    trends_list1=Trends.objects.filter(choice__icontains='national')
    return render(request,'testapp/national.html',{'trends_list1':trends_list1})    

def news_international(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    trends_list=Trends.objects.filter(choice__icontains='international')
    return render(request,'testapp/international.html',{'trends_list':trends_list})      

from . models import Youtube

def youtube_view(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    youtube_list=Youtube.objects.filter(
        Q(title__icontains=q) |
        Q(source_cat__icontains=q)
    )
    return render(request,'testapp/youtube.html',{'youtube_list':youtube_list})

def ybeuty_view(request):
    youtube_list=Youtube.objects.filter(source_cat__icontains='fashionandbeauty')
    return render(request,'testapp/beauty.html',{'youtube_list':youtube_list}) 

def ygaming_view(request):
    youtube_list=Youtube.objects.filter(source_cat__icontains='gaming')
    return render(request,'testapp/game.html',{'youtube_list':youtube_list})

def yvlog_view(request):
    youtube_list=Youtube.objects.filter(source_cat__icontains='vlogs')
    return render(request,'testapp/vlog.html',{'youtube_list':youtube_list})   

def yedu_view(request):
    youtube_list=Youtube.objects.filter(source_cat__icontains='education')
    return render(request,'testapp/edu.html',{'youtube_list':youtube_list})         

def ysports_view(request):
    youtube_list=Youtube.objects.filter(source_cat__icontains='sports')
    return render(request,'testapp/sportz.html',{'youtube_list':youtube_list})  

def yenter_view(request):
    youtube_list=Youtube.objects.filter(source_cat__icontains='entertainment')
    return render(request,'testapp/enter.html',{'youtube_list':youtube_list})  

from . import forms
from django.http import HttpResponseRedirect

def Signup_view(request):
    form=forms.SignUpform()
    if request.method=='POST':
        form=forms.SignUpform(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})


