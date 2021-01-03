from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, FileResponse
from django.template import loader
from .models import Stock

def index(request):
    return render(request, 'stock/index.html')

def database(request):
    context = {}
    template = loader.get_template('stock/database.html')
    return HttpResponse(template.render(context, request))

def db(request):
    response = FileResponse(open('/home/jsheo/AllN/news.db', 'rb'))
    return response

def stock(request, number):
    stock = get_object_or_404(Stock, code=number)
    return render(request, 'stock/stock.html', {'stock':stock})
