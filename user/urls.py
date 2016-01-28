import user
from user.views.user_views import AdditionalInfo, ProfileTakser, Work
from django.conf.urls import url

urlpatterns = \
    [
        url(r'^login/', user.views.user_views.login_user, name='login'),
        url(r'^registration/', user.views.user_views.registration, name='registration'),
        url(r'^$', user.views.user_views.index, name='index'),
        url(r'^logout/$', user.views.user_views.logout_user),
        url(r'^accounts/confirm/(?P<activation_key>\w+)/', user.views.user_views.register_confirm),
        url(r'^work/(?P<customer_id>\d+)/$', Work.as_view(), name='work'),
        url(r'^profile-tasker/(?P<customer_id>\d+)/$', ProfileTakser.as_view(), name='profile_tasker'),
        url(r'^profile-customer/(?P<customer_id>\d+)/$', user.views.user_views.profile_user, name='profile_customer'),
        url(r'^additional-info', AdditionalInfo.as_view(), name='additional_info')
    ]
