from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from django.views.decorators.http import require_http_methods
from django_ratelimit.decorators import ratelimit


@ratelimit(key='ip', rate='5/m', method='POST', block=True)
@require_http_methods(["GET", "POST"])
def register_view(request):
    """
    Handle user registration.
    Authenticates and logs in the user automatically upon successful registration.
    Redirects authenticated users to the home page.
    Rate limited to 5 POST requests per minute per IP.
    """
    if request.user.is_authenticated:
        return redirect('baby:home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('baby:home')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'cadastro.html', {'form': form})


@ratelimit(key='ip', rate='10/m', method='POST', block=True)
@require_http_methods(["GET", "POST"])
def login_view(request):
    """
    Handle user authentication and login.
    Redirects authenticated users to the home page.
    Rate limited to 10 POST requests per minute per IP.
    """
    if request.user.is_authenticated:
        return redirect('baby:home')
    
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo de volta, {user.first_name or user.username}!')
                return redirect('baby:home')
        messages.error(request, 'Email ou senha incorretos.')
    else:
        form = UserLoginForm()
    
    return render(request, 'login.html', {'form': form})


@require_http_methods(["POST"])
def logout_view(request):
    """
    Logout the currently authenticated user and redirect to home.
    Requires POST to prevent CSRF logout via link prefetching.
    """
    logout(request)
    messages.info(request, 'Você foi desconectado com sucesso.')
    return redirect('baby:home')


@login_required
@require_http_methods(["GET", "POST"])
def perfil_view(request):
    """
    Display and handle the user's profile update form.
    Requires authentication. Handles both avatar and data updates.
    """
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('users:perfil')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'users/perfil.html', {'form': form})
