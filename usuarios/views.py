from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Registro de usuario con inicio de sesión automático
def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # inicia sesión automáticamente
            return redirect('menu')  # redirige al menú
    else:
        form = UserCreationForm()
    return render(request, "usuarios/registro.html", {"form": form})

# Login de usuario
def login_usuario(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu')
    else:
        form = AuthenticationForm()
    return render(request, "usuarios/login.html", {"form": form})

# Logout de usuario
def logout_usuario(request):
    logout(request)
    return redirect('login')

# Menú principal (requiere login)
@login_required
def menu(request):
    return render(request, "usuarios/menu.html")

# Consulta de calificaciones
@login_required
def calificaciones(request):
    return render(request, "usuarios/calificaciones.html")

# Avisos / comunidad
@login_required
def avisos(request):
    return render(request, "usuarios/avisos.html")

# Horas de servicio y prácticas
@login_required
def servicio(request):
    return render(request, "usuarios/servicio.html")
