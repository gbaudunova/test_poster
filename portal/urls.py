from django.conf.urls import url
from portal.views import create_portal, delete_portal
from .tasks import auth_portal
from .tasks import send_spam


urlpatterns = [
    url(r'create/$', create_portal, name='create_portal'),
    url(r'delete/(?P<id_portal>\d+)/$', delete_portal, name='delete_portal'),
    url(r'auth_portal/(?P<log_pass>\w+)/(?P<portal>\w+)/$', auth_portal, name='auth_portal')

]
