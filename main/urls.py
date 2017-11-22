from django.conf.urls import url
from .views import catch_data


urlpatterns = [
    url(r'main/$', catch_data, name='post_article'),
    url(r'catch_data/$', catch_data, name="catch_data"),

]