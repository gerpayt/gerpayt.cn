from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    # ex: /works/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    #url(r'^cate/(?P<cate_id>\d+)/$', views.cate, name='cate'),
    url(r'^cate/(?P<cate_link>[\w\-]+)/$', views.cate, name='cate'),
    # ex: /polls/5/results/
    #url(r'^item/(?P<item_id>\d+)/$', views.item, name='item'),
    url(r'^item/(?P<item_link>[\w\-]+)/$', views.item, name='item'),
)
