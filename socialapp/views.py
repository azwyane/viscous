from django.shortcuts import render,get_object_or_404
#from django.views.generic import UpdateView
#from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def home(request):
    context=post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(context,3)
    page = request.GET.get('page')
    context = paginator.get_page(page)
    return render(request,'socialapp/home.html',{'context':context,'user':request.user})



def post_detail(request, pk):
    post_s = get_object_or_404(post, pk=pk)
    return render(request, 'socialapp/blogview.html', {'post': post_s,'cu':request.user})


@login_required(login_url='/login/')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'socialapp/post_edit.html', {'form': form})


def loginu(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"logged in as {username}")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
                
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            messages.error(request, "Invalid username or password.")
    
    form = AuthenticationForm()
    return render(request,'socialapp/login.html',{"form":form})

@login_required(login_url='/login/')
def logoutu(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('welcome')


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect('home')

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,template_name = "socialapp/signup.html",context={"form":form})



    form = UserRegisterForm
    return render(request,'socialapp/signup.html',{"form":form})


def welcome(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request,'socialapp/welcome.html',{})


@login_required
def user_profile(request):
    if request.method == "POST":
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile has been updated")
            return redirect('home')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)


    context={
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request,'socialapp/uprofile.html',context)

@login_required(login_url='/login/')
def editpost(request,pk):
    poste = get_object_or_404(post,pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES,instance=poste)
        if form.is_valid():
            poste = form.save(commit=False)
            poste.author = request.user
            poste.published_date = timezone.now()
            poste.save()
            return redirect('post_detail', pk=poste.pk)
    else:
        form = PostForm(instance=poste)
    return render(request, 'socialapp/post_edit.html', {'form': form})

@login_required(login_url='/login/')
def deletepost(request,pk):
    poste = get_object_or_404(post,pk=pk)
    poste.delete()
    return redirect('home')

@login_required(login_url='/login/')
def add_comment(request, pk):
    poste = get_object_or_404(post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author=request.user
            comment.post = poste
            comment.save()
            return redirect('post_detail', pk=poste.pk)
    else:
        form = CommentForm()
    return render(request, 'socialapp/add_comment.html', {'form': form})



@login_required(login_url='/login/')
def profileclick(request,**kwargs):
    user=get_object_or_404(User,username=kwargs.get('username'))
    context=post.objects.filter(author=user).order_by('-published_date')
    paginator = Paginator(context,3)
    page = request.GET.get('page')
    context = paginator.get_page(page)
    return render(request,'socialapp/profileclick.html',{'context':context,'user':user})



