from django.conf.urls import url, patterns
from rally_dashboard import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)