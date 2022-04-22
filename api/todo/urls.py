from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from todo import views




urlpatterns = [
    path('todos/', views.TodoListApiView.as_view()),
    path('todo/<int:todo_list_id>/', views.ToDoList.as_view()),
    path('todo/items/<int:todo_list_item_id>/', views.ToDoListItem.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)


# from django.urls import include, re_path
# from rest_framework.urlpatterns import format_suffix_patterns
# from todo import views

# urlpatterns = [
# 	# Maps to ToDoList.get and ToDoList.post
# 	re_path(r'^todo_lists$', views.ToDoList.as_view()),
# 	# Maps to ToDoList.delete
# 	re_path(r'^todo_lists/(?P<todo_list_id>[0-9]+)$', views.ToDoList.as_view()),
# 	# maps to ToDoListItem.post
# 	re_path(r'^todo_lists/(?P<todo_list_id>[0-9]+)/items$', views.ToDoListItem.as_view()),
# 	# maps to ToDoListItem.delete
# 	re_path(r'^todo_lists/items/(?P<todo_list_item_id>[0-9]+)$', views.ToDoListItem.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
