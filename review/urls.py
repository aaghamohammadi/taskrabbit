from django.conf.urls import include, url
from django.contrib import admin

from review.review_views import CreateCommentView

urlpatterns = \
    [
        url(r'^create-comment/', CreateCommentView.as_view(), name='create_comment'),

    ]
