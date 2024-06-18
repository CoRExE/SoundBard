from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='accueil'),
    path('soundboards/', views.soundboard_list, name='soundboard.list'),
    path('soundboards/upload', views.upload, name='soundboard.upload'),
    path('soundboards/upload-sound/', views.upload_file, name='soundboard.upload_file'),
    path('soundboards/setting', views.setting, name='soundboard.setting'),
]
