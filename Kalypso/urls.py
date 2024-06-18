from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('credentials/', views.credentials, name='credentials'),
    path('install/', views.install, name='install'),
    path('setup/', views.setup, name='setup'),
    # path('chat/', views.chat, name='chat'),
    # path('logout/', views.logout, name='logout'),
    path('quick-chat/', views.quick_chat, name='quick-chat'),
]
