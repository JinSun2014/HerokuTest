from django.conf.urls import patterns, include, url

from django.contrib import admin

from HerokuTest import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HerokuTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name = 'index'),
)
