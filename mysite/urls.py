from django.conf.urls import url
from django.contrib import admin
from mainapp.views import main, work, education, organization

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main),
    url(r'^work/$', work),
    url(r'^education/$', education),
    url(r'^work/organization/(?P<org_id>\d+)/$', organization)
]
