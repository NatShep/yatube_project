from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def groups_list(request):
    return HttpResponse('Список сообществ')


def group_posts(request, slug):
    return HttpResponse(f'Список постов сообщества {slug}')
