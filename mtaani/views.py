from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,NeighbourHood
from .decorators import unauthenticated_user,allowed_users
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm,PostForm
from django.contrib import messages
from django .contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import DetailView
# Create your views here.


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')


    context = {'form': form}
    return render(request,'accounts/register.html',context)
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username = username,password= password)
        if user is not None:
            login(request,user)
            return redirect('home')
            
        else:
            messages.info(request,'Username or password is inorrect')
            

    context = {}
    return render(request,'accounts/plogin.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')





def userPage(request):
    context = {}

    return render(request,'accounts/user.html',context)



def profile(request):
    user = request.user
    user = Profile.objects.get_or_create(user= request.user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)                         
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user': user

    }

    return render(request, 'accounts/profile.html', context)


@login_required(login_url='login')
def home(request):
    posts = NeighbourHood.objects.all()
    context={"posts":posts}

    return render (request, 'index.html', context)



def viewPhoto(request,pk):
    photo = NeighbourHood.objects.get(id=pk)
    return render(request,'post_detail.html',{'photo':photo})



def create_post(request):
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid:
            post = form.save(commit= False)
            post.author = current_user
            post.save()
        return redirect('home')
    else:
        form = PostForm()
    return render(request,'create_hood.html',{'form':form})



@login_required(login_url='login')
@allowed_users(allowed_roles=[' businessname '])
def accountSettings(request):
	bussiness = request.user. businessname 
	form = PostForm(instance=bussiness)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES,instance=bussiness)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'accounts/userproc.html', context)

def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("home")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)
