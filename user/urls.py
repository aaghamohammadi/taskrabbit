import user
import user.views.user_views
from django.conf.urls import url

urlpatterns = \
    [
        url(r'^login/', user.views.user_views.login_user, name='login'),
        url(r'^registration/', user.views.user_views.registration, name='registration'),
        url(r'^$', user.views.user_views.index, name='index'),
        url(r'^logout/$', user.views.user_views.logout_user, name='logout'),
        url(r'^accounts/confirm/(?P<activation_key>\w+)/', user.views.user_views.register_confirm,
            name='confirm_account'),
        url(r'^profile-customer/(?P<customer_id>\d+)/$', user.views.user_views.profile_user, name='profile_customer'),
        url(r'^edit-customer-profile', user.views.user_views.edit_customer_profile, name='edit-customer-profile')
    ]
