from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from contact.models import Contact


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Welcome')
            return redirect('app-dashboard')
        else:
            messages.error(request, 'invalid username or password')
            return redirect('app-login')
    else:
        return render(request, 'account/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist')
                return redirect('app-register')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is being used ')
                    return redirect('app-register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                    password=password, email=email)
                    user.save()
                    messages.success(request, 'Account created successfully ')
                    return redirect('app-login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('app-register')
    return render(request, 'account/register.html')


def dashboard(request):
    user_contact = Contact.objects.order_by('-message_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contact
    }
    return render(request, 'account/dashboard.html', context)


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        messages.success(request, 'Successfully log out')
        return redirect('app-login')
