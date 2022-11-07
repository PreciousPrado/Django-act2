from django.urls import path

from . import views

urlpatterns = [
path('',views.index, name='index'),
path('test',views.index, name='test'),
path('test2',views.index, name='test2'),
]
