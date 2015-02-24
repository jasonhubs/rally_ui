from django.conf.urls import url, patterns
from rally_dashboard import views
from django.conf import settings
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
