from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import Post,Profile,Comment
from .forms import UserUpdateForm,ProfileUpdateForm,CommentForm,PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

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

# @login_required(login_url='login')
# def user_profile(request,author_id):
#     try:
#         profiles = Profile.get_profile_by_id(id=author_id)
#         print(profile)
#     except ObjectDoesNotExist:
#         raise Http404()
#         raise False

#     return render(request, 'profiles.html', {'profiles':profiles})

@login_required(login_url='login')
def post_comment(request,pk):
    post = Post.get_post(pk)
    comments = Comment.get_comment(post.id)
    if request.method == 'POST':
        c_form = CommentForm(request.POST,instance=request.user)
        if c_form.is_valid():
            comment = c_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_comment', post_id = post_id)
    else:
        c_form = CommentForm(instance=request.user)

    context = {
        'c_form':c_form,
        'comments':comments,
        'post':post
    }
    return render(request, 'comment.html', context)

@login_required(login_url='login')      
def upload_post(request):
    """
    view functon displays the upload post form
    """
    profiles = Profile.objects.all()
    current_user = request.user.profile
    for profile in profiles:
        if profile.user.id == request.user.id:
            if request.method == 'POST':
                form = PostForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.profile = current_user
                    post.save()
                return redirect('profile', profile_id=profile.id)
            else:
                form = PostForm()
    return render(request, 'upload_post.html', {'form':form, 'profiles':profiles})