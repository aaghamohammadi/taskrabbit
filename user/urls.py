from user.views.user_views import AdditionalInfo, ProfileCustomer
from django.conf.urls import url

urlpatterns = \
    [
        url(r'^login/', 'user.views.user_views.login_user', name='login'),
        url(r'^registration/', 'user.views.user_views.registration', name='registration'),
        url(r'^$', 'user.views.user_views.index', name='index'),
        url(r'^logout/$', 'user.views.user_views.logout_user'),
        url(r'^profile-customer/(?P<customer_id>\d+)/$', ProfileCustomer.as_view(), name='profile_customer'),
        url(r'^additional-info', AdditionalInfo.as_view(), name='additional_info')
    ]
