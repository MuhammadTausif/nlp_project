from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1', views.index, name='index'),
    path('2', views.index1, name='index'),
    path('2', views.index2, name='index'),
    path('3', views.index3, name="good")
]