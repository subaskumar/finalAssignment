from django.shortcuts import render,redirect
from Auth_App.forms import SignUpForm,UserLoginForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    users = User.objects.select_related('logged_in_user')
    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'
    return render(request,'Auth_App/home.html',{'users': users})
def sinUp_view(request):
    message = ''
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            form = SignUpForm()
            message = 'Registration Successfull'
        return render(request,'Auth_App/signUp.html',{'form':form,'message': message})
    
    else:
        form = SignUpForm()        
        return render(request,'Auth_App/signUp.html',{'form':form,'message': message})

def login_view(request):
        form = UserLoginForm()
        if request.method == "POST":
            form = UserLoginForm(request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request,username=username, password=password)
                login(request, user)
                return redirect('/home')
        return render(request, 'Auth_App/LogIn_form.html',{'form':form})
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')