from service.service_views import EditSkillView, TaskerProfileView, ShowSkillView, ShowCategoriesView, ShowCustomersOrders, \
    ShowCategorySkills, ShowSkillsView, ShowTaskersView, ShowFactorView, RecordOrderView
from django.conf.urls import url

__author__ = 'garfild'

urlpatterns = \
    [
        url(r'^show_categories/$', ShowCategoriesView.as_view(), name='show_categories'),
        url(r'^show-category-skills/(?P<category_id>\d+)/', ShowCategorySkills.as_view(),
            name='show_category_skills'),
        url(r'edit-skill/', EditSkillView.as_view(), name='edit_skill'),
        url(r'show-my-skills/$', TaskerProfileView.as_view(), name='show_my_skills'),
        url(r'tasker-profile/(?P<tasker_id>\d+)/$', TaskerProfileView.as_view(), name='tasker_profile'),
        url(r'show-skills/$', ShowSkillsView.as_view(), name='show_skills'),
        url(r'show-skill/(?P<tasker_id>\d+)/(?P<skill_id>\d+)/$', ShowSkillView.as_view(), name='show_skill'),
        url(r'show-customers-orders/', ShowCustomersOrders.as_view(), name='show_customers_orders'),
        url(r'show-taskers/', ShowTaskersView.as_view(), name='show_taskers'),
        url(r'show-factor/(?P<skill_id>\d+)/', ShowFactorView.as_view(), name='show_factor'),
        url(r'record-order/(?P<skill_id>\d+)/', RecordOrderView.as_view(), name='record_order')
    ]
