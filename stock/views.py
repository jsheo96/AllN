from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, FileResponse
from django.template import loader
from .models import Stock

def index(request):
#    stock = get_object_or_404(Stock, code=number)
    if request.method == "POST":
        company_name = request.POST["comp_name"]
#        form = 
#        if form.is_valid():
#            form.save()
#            return redirect('')
#        else:
        return render(request, 'stock/index.html', {"comp_name": company_name})
    else:
#        company_name = request.GET.get["comp_name"]
#        print(company_name)
#        form = 
        company_name = request.GET.get('comp_name')
        return render(request, 'stock/index.html', {"comp_name": company_name})

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
