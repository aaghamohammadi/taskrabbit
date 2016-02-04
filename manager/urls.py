from django.conf.urls import url
from manager.views.manager_views import CreateCategoryView, ShowCategoriesView, ShowUsersView

urlpatterns = \
    [
        url(r'^$', CreateCategoryView.as_view(), name='index'),
        url(r'^show-categories/$', ShowCategoriesView.as_view(), name='show_categories'),
        url(r'^show-users/$', ShowUsersView.as_view(), name='show_users')
    ]
