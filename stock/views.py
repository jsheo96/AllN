from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, FileResponse
from django.template import loader


def index(request):
    return render(request, 'stock/index.html')

def database(request):
    context = {}
    template = loader.get_template('stock/database.html')
    return HttpResponse(template.render(context, request))

def db(request):
    response = FileResponse(open('/home/jsheo/AllN/news.db', 'rb'))
    return response
