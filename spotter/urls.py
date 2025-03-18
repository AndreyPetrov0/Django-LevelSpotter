from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/index_1', views.index_1, name='index_1'),
    path('/index_2', views.index_2, name='index_2'),
    path('/index_3', views.index_3, name='index_3'),
]