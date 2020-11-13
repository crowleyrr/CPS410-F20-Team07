from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.template import loader

from .models import Student
# Create your views here.
class StartingPageView(TemplateView):
    """
    View for the page the user sees upon reaching the site before logging in.
    """
    template_name = 'users/startingpage.html'
    # student = Student.objects.filter().first()
    # context = {'student_name': student.first_name}
    # # return render(request, template_name, {})

def index(request):
    return HttpResponse("MADE IT TO USER INDEX.")
