from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import Post,Profile,Comment
from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def index(request):
    """
    view function renders the landing page
    """
    posts = Post.display_posts()
    return render(request, 'index.html', {'posts':posts})

def search_results(request):
    """
    view function returns the searched users
    """
    if 'profile' in request.GET and request.GET["profile"]:
        user_search = request.GET.get("profile")
        searched_users = Profile.get_user_by_profile(user_search)
        message = f"{user_search}"

        return render(request, 'search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any user"
        return render(request, 'search.html',{"message":message})

        
@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save() 
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)
