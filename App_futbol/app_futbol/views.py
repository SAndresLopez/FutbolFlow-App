from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from .models import Partido, Inscripcion, PerfilJugador


def home(request):
    partidos = Partido.objects.all()
    return render(request, 'home.html', {'partidos': partidos})

@login_required
def unirse_partido(request, partido_id):
    partido = get_object_or_404(Partido, id=partido_id)

    ya_inscrito = Inscripcion.objects.filter(usuario=request.user, partido=partido).exists()

    if ya_inscrito:
        messages.warning(request, "Ya estás en la lista para esta pichanga.")
    elif partido.cupos_inscritos < 12:
        Inscripcion.objects.create(usuario=request.user, partido=partido)

        partido.cupos_inscritos += 1
        partido.save()
        messages.success(request, "¡Fichado! Prepárate para el partido.")
    else:
        messages.error(request, "Cancha llena, ya están los 12.")

    return redirect('home')


@csrf_exempt
def completar_perfil(request):
    print("🚀 ¡ENTRÉ A LA VISTA!")
    user = request.user

    if not user.is_authenticated:
        data = request.session.get('socialaccount_sociallogin')
        if isinstance(data, dict):
            email = data.get('user', {}).get('email')
            print(f"📧 Identificado por sesión: {email}")

            user, created = User.objects.get_or_create(
                email=email,
                defaults={'username': email.split('@')}
            )
            if created:
                print(f"👤 NUEVO USUARIO CREADO: {user.username}")

    if not user or user.is_anonymous:
        print("❌ ERROR: Sigo sin usuario. Revisa la sesión.")
        return redirect('/accounts/google/login/')

    if request.method == 'POST':
        print(f"📩 ¡RECIBÍ UN POST PARA: {user.email}!")

        if not user.pk:
            user.save()

        perfil, created = PerfilJugador.objects.get_or_create(usuario=user)
        perfil.apodo = request.POST.get('apodo')
        perfil.telefono = request.POST.get('telefono')
        perfil.posicion = request.POST.get('posicion')
        perfil.distrito = request.POST.get('distrito')
        perfil.save()

        print("✅ PERFIL GUARDADO EXITOSAMENTE")

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')

    return render(request, 'socialaccount/signup.html', {'user': user})