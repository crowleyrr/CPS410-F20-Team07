from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.template import loader

# Create your views here.
def StartingPageView(request):
    """
    View for the page the user sees upon reaching the site before logging in.
    """
    template_name = loader.get_template('users/startingpage.html')
    context = {}
    return HttpResponse(template.render(null, request))

def index(request):
    return HttpResponse("MADE IT TO USER INDEX.")
