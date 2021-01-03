from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('database', views.database, name='database'),
    path('news.db', views.db, name='db'),
    path('<int:number>', views.stock, name='stock')
]