from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404


# Create your views here.
def index(request):
    """
    view function renders the landing page
    """
    return render(request, 'index.html')