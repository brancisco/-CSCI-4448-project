from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('ajax_wait', views.wait, name='waitPage'),
]
