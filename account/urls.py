from django.conf.urls import url
from .views import register_user, authorization_user, logout_user

urlpatterns = [
    url(r'register/$', register_user, name='register user'),
    url(r'login/$', authorization_user, name='authorization user'),
    url(r'logout/$', logout_user, name='logout user'),
]

