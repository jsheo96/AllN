from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, FileResponse
from django.template import loader
from .models import Stockdb, Issuedb, Newsdb

import json

stocks = Stockdb.objects.all()
issues = Issuedb.objects.all()
news = Newsdb.objects.all()


def newsFind(issue_id):
    data_dict = json.loads(issues[int(issue_id)].data)
    news_numbers = data_dict['news']
    news_data_dict_list = []
    news_dict_list = []
    
    for news_number in news_numbers:
        news_data_dict = json.loads(news[news_number].data)
        news_data_dict_list.append(news_data_dict)
        news_dict_list.append(news[news_number])
    return(news_data_dict_list)



def issueFind(stock_id):
    data_dict = json.loads(stocks[int(stock_id)].data)
    issue_numbers = data_dict['issues']
    issue_obj_list = []
    
    for issue_number in issue_numbers:
        issue_obj_list.append(issues[issue_number])
#        issue_data = json.loads(issues[issue_number].data)
#        추후 날짜 고려할 때 
    return(issue_obj_list)



def index(request):
    return render(request, 'stock/index.html', {"stocks": stocks})
    

def stock(request, stock_id): 
    stock_obj = get_object_or_404(Stockdb, stock_id=stock_id)
    stock_name = stock_obj.name
    issue_obj_lists = issueFind(stock_id)

    try: 
        if (request.method == "POST"):
            return render(request, 'stock/stock.html', {"stocks": stocks,"stock_obj": stock_obj, "issue_obj_lists": issue_obj_lists})
    except: return render(request, 'stock/stock.html', {"stocks": stocks,"stock_obj": stock_obj}) 
    
    return render(request, 'stock/stock.html', {"stocks": stocks,"stock_obj": stock_obj, "issue_obj_lists": issue_obj_lists})



def issue(request, stock_id, issue_id):
    stock_obj = get_object_or_404(Stockdb, stock_id=stock_id)
    issue_obj_lists = issueFind(stock_id)
    issue_obj = get_object_or_404(Issuedb, issue_id=issue_id)
    news_objs = newsFind(issue_id)
    
    if issue_obj not in issue_obj_lists:
        raise Http404("Question does not exist")
#    stock_obj에 대한 해당 issue가 없으면 404 err

    
    return render(request, 'stock/issue.html', {"stocks": stocks, "stock_obj": stock_obj, "issue_obj_lists": issue_obj_lists, 'issue_obj': issue_obj, 'news_objs': news_objs})





def database(request):
    context = {}
    template = loader.get_template('stock/database.html')
    return HttpResponse(template.render(context, request))

def db(request):
    response = FileResponse(open('/home/jsheo/AllN/news.db', 'rb'))
    return response
