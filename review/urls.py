from django.conf.urls import include, url
from django.contrib import admin

from review.review_views import CreateCommentView, CreateRateView

urlpatterns = \
    [
        url(r'^create-comment/', CreateCommentView.as_view(), name='create_comment'),
        url(r'^create-rate/', CreateRateView.as_view(), name='create_rate')

    ]
