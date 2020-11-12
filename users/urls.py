from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from users.views import HomePageView

urlpatterns = [
    url(r'^home/$', TemplateView.as_view(template_name="Home.html")),
    url(r'^appointments/$', TemplateView.as_view(template_name="Appointment.html")),
    url(r'^courses/$', TemplateView.as_view(template_name="Courses.html")),
    url(r'^profile/$', TemplateView.as_view(template_name="Profile.html")),
    url(r'^recommend/$', TemplateView.as_view(template_name="Recommend.html")),
    url(r'^schedule/$', TemplateView.as_view(template_name="Schedule.html")),
    url(r'^search/$', TemplateView.as_view(template_name="Search.html")),

    url(r'^$', views.index, name='index'),

]
