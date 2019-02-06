
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Post1, Profile
from .forms import PostCreateForm, UserLoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def post_list(request):
    posts= Post1.objects.all()
    context={
    'posts':posts,
    }
    return render (request,'blog/post_list.html',context)

def post_detail(request, id, slug):
    post = get_object_or_404(Post1,id=id, slug=slug)
    context = {
        'post': post,
    }
    return render (request, 'blog/post_detail.html', context)

def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostCreateForm()
    context = {
        'form': form,
    }
    return render (request, 'blog/post_create.html', context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('post_list'))
                else:
                    return HttpResponse("User is not active")
            else:
                return HttpResponse("User is None")
    else:
        form = UserLoginForm()
    context = {
        'form':form,
    }
    return render (request,'blog/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('post_list')

def register(request):
    try:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST or None)
            if form .is_valid():
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                Profile.objects.Create(user=new_user)
                return redirect('post_list')
        else:
            form = UserRegistrationForm()
        context = {
            'form':form,
        }
        return render(request, 'registration/register.html', context)
    except Exception as e:
        print (e)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(data = request.POST or None,instance = request.user)
        profile_form = ProfileEditForm(data= request.POST or None, instance= request.user.profile,files= request.FILES)
        if user_form.is_valid()and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance= request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)

    context ={
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request,'blog/edit_profile.html',context)
