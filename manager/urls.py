from manager.views.manager_views import EditTask, ModelTaskList, DeleteTask

__author__ = 'garfild'

from django.conf.urls import url

urlpatterns = \
    [
        url(r'edit-task/$', EditTask.as_view(), name='edit_task'),
        url(r'model-task-list/$', ModelTaskList.as_view(), name='task_model_list'),
        url(r'delete-task-model/(?P<task_model_id>\d+)/$', DeleteTask.as_view(), name='delete_task_model')
    ]
