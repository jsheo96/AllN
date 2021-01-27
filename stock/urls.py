from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('stock/<int:stock_id>', views.stock, name='stock'),
    path('stock/<int:stock_id>/issue/<int:issue_id>', views.issue, name='issue'),
    
    path('database', views.database, name='database'),
    path('news.db', views.db, name='db'),
#    path('<int:number>', views.stock, name='stock')
]