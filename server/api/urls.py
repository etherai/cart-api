from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
     url(r'^api/v1/', include('api.cart_api.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
