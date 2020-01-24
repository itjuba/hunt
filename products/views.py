from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import  JsonResponse
from .models import Product
from django.utils import  timezone

import json
# Create your views here.
def ajax(request):
    product = Product.objects
    return render(request, 'ajax.html',{'product': product})


def home(request):
    product = Product.objects
    return render(request,'products/home.html' ,{'product': product})

@login_required(login_url='/accounts/signup')
def addp(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and \
                request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']

            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.image = request.FILES['image']
            product.icon = request.FILES['icon']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))

        else:
            return render(request, 'products/home.html', {'error': 'all fields are required !'})
    return render(request,'products/add_product.html')

def detail(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html',{'product':product})

@login_required(login_url='/accounts/signup')
def upvote(request):

    if request.method == 'POST':
        # id = request.POST.get('product_id')
        ans_id = json.loads((request.body.decode('utf-8')))
        id = ans_id["product_id"]
        print(id)



    if id:
        product = get_object_or_404(Product,pk=id)
        if product:
          product.votes_total+=1
          product.save()


          return JsonResponse({'likes': product.votes_total})


def homeupvote(request,product_id):
    product = Product.objects
    return render(request,'home',{'product:product'})

