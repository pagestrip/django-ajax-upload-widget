from django.conf.urls import url

from ajax_upload.views import upload

urlpatterns = (
    #'ajax_upload.views',
    url(r'^$', upload, name='ajax-upload'),
)
