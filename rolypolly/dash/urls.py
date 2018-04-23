from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('create/', views.create, name='create'),
	path('ajax_save_poll', views.save_poll, name='save_poll'),
	path('ajax_update_poll', views.update_poll, name='update_poll'),
	path('review/<int:poll_id>', views.review, name='review')
]
