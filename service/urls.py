from service.service_views import EditSkillView

__author__ = 'garfild'

from django.conf.urls import url

urlpatterns = \
    [
        # url(r'^show_categories/$', ShowCategories.as_view(), name='show_categories'),
        # url(r'^show-taskers/(?P<task_model_id>\d+)/', ShowTaskers.as_view(), name='show_taskers')
        url(r'edit-skill/', EditSkillView.as_view(), name='edit_skill')
    ]
