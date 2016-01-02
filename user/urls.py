from user.views.user_views import AdditionalInfo
from django.conf.urls import url

urlpatterns = \
    [
        url(r'^login/', 'user.views.user_views.login_user', name='login'),
        url(r'^registration/', 'user.views.user_views.registration', name='registration'),
        url(r'^$', 'user.views.user_views.index', name='index'),
        url(r'^additional-info', AdditionalInfo.as_view(), name='additional_info')
    ]
