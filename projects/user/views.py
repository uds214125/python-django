from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index():
    pass

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("email ======", username)
        print("password=======", password)
        
        creds = auth.authenticate(username=username, password=password)
        if creds is not None:
            auth.login(request, creds)
            return render(request, 'home.html')
        else:
            print("creds=======:",creds)
            messages.info(request, 'Something went wrong , check your credentials.')
            return redirect("signin")
    else:
        return render(request, "signin.html", {'title':"signin"})
    
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = first_name + " "+ last_name
        email = request.POST['email']
        password = request.POST['password']
        cnf_password = request.POST['cnf_password']
        if password == cnf_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username exist')
                return redirect("signup");
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email exist')
                return redirect("signup");
            else:
                print("=============username ============", username)
                user = User.objects.create_user(username=username,
                                                password=password,
                                                email=email,
                                                first_name=first_name,
                                                last_name=last_name,
                                                is_active=True)
                user.save();
        else:
            messages.info(request, 'Password and Confirm Password did not match')
            return redirect("signup");
        return redirect("signin");
    else:
        return render(request, "signup.html", {'title':"signup"})
    
def signout(request):
    auth.logout(request)
    return redirect("/signin")

def home(request):
    return render(request, 'home.html')