from django.conf.urls import patterns, url
from apps.blog import views


urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^posts/$', views.post_list, name="post_list"),
    url(r'^post/(?P<id>\d+)/$', views.post_detail, name="post_detail"),
    url(r'^edit-post/$', views.post_form, name="post_form"),
    url(r'^edit-post/(?P<id>\d*)/$', views.post_form, name="post_form"),
)
