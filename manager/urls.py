from manager.views.manager_views import EditTask, ModelTaskList

__author__ = 'garfild'

from django.conf.urls import url

urlpatterns = \
    [
        url(r'edit-task/$', EditTask.as_view(), name='edit_task'),
        url(r'model-task-list/$', ModelTaskList.as_view(), name='task_model_list')
    ]
