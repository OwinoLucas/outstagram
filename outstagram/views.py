from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404, HttpResponseRedirect, JsonResponse
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
    # comments = Comment.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES,instance=request.user.profile)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm(instance=request.user.profile)
        
        
    return render(request, 'index.html', {'posts':posts, 'form':form})

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
   # posts = request.user.username.author.all()
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
        'p_form': p_form,
        #'posts':posts
        
    }
    return render(request, 'profile.html', context)

# @login_required(login_url='login')
# def user_profile(request,username):
#     prof = get_object_or_404(User, username=username)
#     if request.user == prof:
#         return redirect('profile', username=request.user.username)
#     post = prof.user.posts.all()
#     context = {
#         'prof':prof,
#         'post':post
#     }

#     return render(request, 'profiles.html',context)

@login_required(login_url='login')
def post_comment(request,post_id):
    post = get_object_or_404(Post, id =post_id)
    current_user = request.user
    if request.method == 'POST':
        c_form = CommentForm(request.POST, request.FILES)
        if c_form.is_valid():
            comment = c_form.save(commit=False)
            comment.user = current_user
            comment.post = post
            comment.save()
            return redirect('index')
    else:
        c_form = CommentForm()
  
    return render(request, 'comment.html', {'c_form':c_form, 'post_id':post_id})

@login_required(login_url='login')      
def upload_post(request):
    """
    view functon displays the upload post form
    """
    profiles = Profile.objects.all()
    current_user = request.user
    for profile in profiles:
        if profile.user.id == request.user.id:
            if request.method == 'POST':
                form = PostForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.profile = current_user
                    post.save()
                return redirect('index')
            else:
                form = PostForm()
    return render(request, 'upload_post.html', {'form':form, 'profiles':profiles})