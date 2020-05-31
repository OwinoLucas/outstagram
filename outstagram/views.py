from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    """
    view function renders the landing page
    """
    return render(request, 'index.html')

# def login(request):
#     """
#     view function renders the template that contains the login form
#     """
#     return render(request, 'registration/login.html')