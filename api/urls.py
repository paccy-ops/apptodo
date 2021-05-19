from django.urls import path
from . import views

urlpatterns = [
    path('todos/completed/', views.TodoCompletedList.as_view(), name='completed'),
    path('todos/', views.TodoListCreate.as_view(), name='todos'),
    path('todos/<int:pk>/', views.TodoRetrieveUpdateDestroy.as_view(), name='todos-actions'),
    path('todos/<int:pk>/complete/', views.TodoComplete.as_view(), name='todos-actions'),

    # auth
    path('signup', views.signup, name='signup'),
    path('login', views.login, name="login")

]
