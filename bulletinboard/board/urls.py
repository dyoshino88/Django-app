from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
  path('create_topic', views.create_topic, name='create_topic'),
  path('list_topics', views.list_topics, name='list_topics'),
  path('edit_topic/', views.edit_topic, name='edit_topic'),
  path('delete_topic/', views.delete_topic, name='delete_topic'),
  path('post_texts/', views.post_texts, name='post_texts'), 
  path('save_text', views.save_text, name='save_text'),
]