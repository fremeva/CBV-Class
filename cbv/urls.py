from django.conf.urls import url

from cbv.views import CBVDetailView, CBVFormView, CBVCreateView, CBVUpdateView, CBVDeleteView
from .views import CBVTemplateViewExample, CBVListUsers

urlpatterns = [
    url(r'^template/$', CBVTemplateViewExample.as_view()),
    url(r'^list/$', CBVListUsers.as_view(), name="list"),
    url(r'^user/(?P<id>\d+)/$', CBVDetailView.as_view()),
    url(r'^form/$', CBVFormView.as_view()),
    url(r'^create/$', CBVCreateView.as_view()),
    url(r'^update/(?P<pk>\d+)/$', CBVUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/', CBVDeleteView.as_view(), name='delete')
]
