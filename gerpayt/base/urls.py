from django.conf.urls import patterns, include, url, static
from django.contrib import admin

from . import settings

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'base.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)),

    url(r'^works/', include('works.urls', namespace='works')),
    url(r'^books/', include('books.urls', namespace='books')),
    url(r'^resume/', include('resume.urls', namespace='resume')),
    url(r'', include('resume.urls', namespace='resume')),
    url(r'^admin/', include(admin.site.urls)),

)
