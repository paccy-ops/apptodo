from django.urls import path
from . import views

urlpatterns=[
    path('todos/completed/',views.TodoCompletedList.as_view(),name='completed'),
    path('todos/',views.TodoListCreate.as_view(),name='todos')

]