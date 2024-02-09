from django.urls import path
from .views import TaskView, TaskDetail, CreateTask, EditTask, DeleteTask, LogIn, LogOut


urlpatterns = [
    path('login/', LogIn.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),

    path('', TaskView.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='tasks'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('edit-task/<int:pk>/', EditTask.as_view(), name='edit-tasks'),
    path('delete-task/<int:pk>', DeleteTask.as_view(), name='delete-task')
    
]