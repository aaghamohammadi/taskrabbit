from django.conf.urls import url
from manager.views.manager_views import CreateCategoryView, ShowCategoriesView, ShowUsersView, DeleteUserView

urlpatterns = \
    [
        url(r'^$', CreateCategoryView.as_view(), name='index'),
        url(r'^show-categories/$', ShowCategoriesView.as_view(), name='show_categories'),
        url(r'^show-users/$', ShowUsersView.as_view(), name='show_users'),
        url(r'^delete-user/(?P<member_id>\d+)/', DeleteUserView.as_view(), name='delete_user')
    ]
