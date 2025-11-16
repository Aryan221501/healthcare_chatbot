from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='chat_index'),
    path('api/message/', views.message_api, name='message_api'),
]
