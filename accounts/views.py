from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from accounts.forms import UserRegisterForm


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        form = UserRegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your account has been created! Please log in.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'Registration failed: {e}')
        else:
            messages.error(request, 'Please correct the errors below.')

        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            display_name = user.get_full_name() or user.username
            messages.success(request, f'Welcome back, {display_name}!')
            if user.is_staff:
                return redirect('ownerhome')
            return redirect('userhome')

        messages.error(request, 'Account does not exist or invalid credentials. Please try again.')
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'index.html')

    def post(self, request):
        logout(request)
        return render(request, 'index.html')
