from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.template import loader

from .models import Student
# Create your views here.
class StartingPageView(TemplateView):
    """
    This view renders the template that is the page the user sees upon arriving
    to the site.
    """
    template_name = 'users/startingpage.html'
    # student = Student.objects.filter().first()
    # context = {'student_name': student.first_name}
    # # return render(request, template_name, {})

class HomePageView(TemplateView):
    """
    This view renders the template for the home page. The user must be logged in
    to see this page.  This is the main page of the site from which the user can
    navigate to other pages.
    """
    template_name = 'Home.html'
    # student = Student.objects.filter().first()
    # context = {'student_name': student.first_name}
    # # return render(request, template_name, {})
