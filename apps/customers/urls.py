from django.conf.urls import url, include

from .views import index, CustomerViewSet


urlpatterns = [
    url(r'^$', index),
]