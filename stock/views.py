from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, FileResponse
from django.template import loader
from .models import Stockdb, Issuedb, Newsdb

import json

stocks = Stockdb.objects.all()
issues = Issuedb.objects.all()
news = Newsdb.objects.all()


def issueFind(stock_id):
    data_dict = json.loads(stocks[int(stock_id)].data)
    issue_numbers = data_dict['issues']
    issue_list = []
    
    for issue_number in issue_numbers:
        
        issue_list.append(issues[issue_number].issue)
        issue_data = json.loads(issues[issue_number].data)
    return(issue_list)



def index(request):
    return render(request, 'stock/index.html', {"stocks": stocks})
    

def stock(request): 
    try: 
        if (request.method == "POST"):
            stock_search = request.POST["stock_name"]
            print(stock_search)
            stock_info = stock_search.split()
            stock_name = stock_info[0]
            stock_id = stock_info[1]
            issue_list = issueFind(stock_id)

            return render(request, 'stock/stock.html', {"stocks": stocks,"stock_name": stock_name, "issues": issue_list})
    except: return redirect('index')  


def database(request):
    context = {}
    template = loader.get_template('stock/database.html')
    return HttpResponse(template.render(context, request))

def db(request):
    response = FileResponse(open('/home/jsheo/AllN/news.db', 'rb'))
    return response
