# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком страниц сообществ
    path('groups/', views.groups_list),
    # Страница для отображениz сообщений группы
    path('group/<slug:slug>/', views.group_posts),
  ] 