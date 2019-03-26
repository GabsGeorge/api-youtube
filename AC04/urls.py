from django.contrib import admin
from django.urls import path
from core import views
from django.conf.urls import url, include

urlpatterns = [

	path('admin/', admin.site.urls, name='admin'),

	path('', views.IndexView.as_view(), name='index'),

	path('index/', views.IndexView.as_view(), name='index'),




	]


