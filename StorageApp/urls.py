from django.conf.urls import patterns, include, url
import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'StorageApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'))
    url(r"^$",views.home),
    url(r'^admin/', include(admin.site.urls)),
)
