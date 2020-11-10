from django.conf.urls import url

from . import views
from users.views import StartingPageView

urlpatterns = [
    url(r'^home/$', views.StartingPageView, name='startingpage'),
    url(r'^$', views.index, name='index'),

]
