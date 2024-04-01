from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_todo/<int:todoid>', views.update_todo, name='update_todo'),
    path('delete_todo/<int:todoid>', views.delete_todo, name='delete_todo'),
]
