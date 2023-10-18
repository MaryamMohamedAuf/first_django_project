from django.shortcuts import render
from django.http import HttpResponse
from.models import product

# Create your views here.

def index(request):
  # return HttpResponse('home')
  #return render(request, 'pages/index.html')
    pass

def about(request):
  pass
   # return HttpResponse('about us')

def contact(request):
  pass
    #return HttpResponse('contact us')

def products(request):
 # return render(request, 'products/products.html')
 pass

def products(request):
    all_products = product.objects.all()
    return render(request, 'products/products.html', {'products': all_products})
