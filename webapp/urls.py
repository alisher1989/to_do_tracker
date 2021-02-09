from django.urls import path

from webapp.views import ToDoListView, TaskCreateView, CreateCategoryView, TaskDeleteView, CompletedTasksView, \
    DetailTaskView, TaskReallyDelete

urlpatterns = [
    path('', ToDoListView.as_view(), name="list"),
    path('completed_tasks/', CompletedTasksView.as_view(), name="completed_tasks"),
    path('create/', TaskCreateView.as_view(), name="create"),
    path('create_category/', CreateCategoryView.as_view(), name="create_category"),
    # path('task/<str:pk>/', DetailTaskView.as_view(), name='detail_task'),
    # path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('complete/<int:pk>/', TaskDeleteView.as_view(), name="delete"),
    path('delete/<int:pk>/', TaskReallyDelete.as_view(), name="really_delete"),
    path('task/<int:pk>/', DetailTaskView.as_view(), name="task_detail"),
]