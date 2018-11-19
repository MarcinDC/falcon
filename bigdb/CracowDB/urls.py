from django.urls import path
from . import views

urlpatterns = [
	path('', views.kw_list, name='kw_list'),
]