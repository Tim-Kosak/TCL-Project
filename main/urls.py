from django.urls import path

from . import views

urlpatterns = [
    path('route/', views.getRoute, name='getRoute'),
    path('', views.index, name='index')
]