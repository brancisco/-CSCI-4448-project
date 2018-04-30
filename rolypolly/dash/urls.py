from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('create/', views.create, name='create'),
	path('ajax_save_poll', views.save_poll, name='save_poll'),
	path('ajax_update_poll', views.update_poll, name='update_poll'),
	path('review/<int:poll_id>', views.review, name='review'),
	path('ajax_delete_poll/<int:poll_id>', views.delete_poll, name='delete_poll'),
	path('ajax_launch_poll', views.launch_poll, name='launch_poll'),
	path('launch', views.launch_page, name='launch'),
	path('ajax_change_question', views.change_question, name='change_question'),
	path('ajax_close_poll', views.close_poll, name='close_poll'),
	path('ajax_check_submissions', views.check_submissions, name='check_submissions'),
]
