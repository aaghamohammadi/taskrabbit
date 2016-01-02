from service.service_views import ShowCategories

__author__ = 'garfild'

from django.conf.urls import url

urlpatterns = \
    [
        url(r'^show_categories$', ShowCategories.as_view(), name='show_categories')
    ]
