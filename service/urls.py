from service.service_views import EditSkillView, ShowSkillsView, ShowSkillView
from django.conf.urls import url

__author__ = 'garfild'

urlpatterns = \
    [
        # url(r'^show_categories/$', ShowCategories.as_view(), name='show_categories'),
        # url(r'^show-taskers/(?P<task_model_id>\d+)/', ShowTaskers.as_view(), name='show_taskers')
        url(r'edit-skill/', EditSkillView.as_view(), name='edit_skill'),
        url(r'show-my-skills/$', ShowSkillsView.as_view(), name='show_my_skills'),
        url(r'show-skills/(?P<tasker_id>\d+)/$', ShowSkillsView.as_view(), name='show_skills'),
        url(r'show-skills/(?P<tasker_id>\d+)/(?P<skill_id>\d+)$', ShowSkillView.as_view(), name='show_skills')

    ]
