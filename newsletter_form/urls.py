from django.conf.urls import url

from .views import SubscribeUserView


urlpatterns = [
    url(r'^subscribe/$', SubscribeUserView.as_view(), name='newsletter_form_subscribe_user'),
]
