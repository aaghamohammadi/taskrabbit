from user.views.user_views import AdditionalInfo
from django.conf.urls import url

urlpatterns = \
    [

        url(r'^additional-info', AdditionalInfo.as_view(), name='additional_info')
    ]
