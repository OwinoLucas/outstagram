from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import Post,Profile,Comment

# Create your views here.
@login_required(login_url='login')
def index(request):
    """
    view function renders the landing page
    """
    return render(request, 'index.html')

def search_results(request):
    """
    view function returns the searched categories
    """
    if 'profile' in request.GET and request.GET["profile"]:
        user_search = request.GET.get("profile")
        searched_users = Post.search_user_by_profile(user_search)
        message = f"{user_search}"

        return render(request, 'search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any user"
        return render(request, 'search.html',{"message":message})

