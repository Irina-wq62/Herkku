from django.shortcuts import render
from  .models import product

def index(request):
    return render(request, "index.html")

def product(request):
    return render(request, "product.html")



# Create your views here.
