from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('init_participant', views.init_participant, name='index'),
]
