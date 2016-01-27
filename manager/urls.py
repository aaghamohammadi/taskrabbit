# from manager.views.manager_views import EditTask, ModelTaskList, DeleteTask, TaskerVerification, DeleteTasker, \
#     TaskerRegistration
#
# __author__ = 'garfild'
#
# from django.conf.urls import url
#
# urlpatterns = \
#     [
#         url(r'edit-task/$', EditTask.as_view(), name='edit_task'),
#         url(r'model-task-list/$', ModelTaskList.as_view(), name='task_model_list'),
#         url(r'delete-task-model/(?P<task_model_id>\d+)/$', DeleteTask.as_view(), name='delete_task_model'),
#         url(r'verification/$', TaskerVerification.as_view(), name='verification_task'),
#         url(r'delete-tasker/(?P<tasker_id>\d+)/$', DeleteTasker.as_view(), name='delete_tasker'),
#         url(r'tasker-registration', TaskerRegistration.as_view(), name='tasker_registration')
#     ]
