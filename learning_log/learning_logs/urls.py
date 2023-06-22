"""Определяет схемы URL для learning_logs"""

from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех тем
    path('topics/', login_required(views.topics), name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', login_required(views.topic), name='topic'),
    # Страница для добавления новой темы
    path('new_topic/', login_required(views.new_topic), name='new_topic'),
    # Страница для добавления новой записи
    path('new_entry/<int:topic_id>/', login_required(views.new_entry), name='new_entry'),
    # Страница для редактирования записи
    path('edit_entry/<int:entry_id>/', login_required(views.edit_entry), name='edit_entry'),
]