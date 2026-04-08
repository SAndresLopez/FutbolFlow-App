from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Partido, Inscripcion


def home(request):
    partidos = Partido.objects.all()

    distrito_filtrado = request.GET.get('distrito')

    if distrito_filtrado:
        partidos = partidos.filter(lugar__icontains=distrito_filtrado)

    return render(request, 'home.html', {'partidos': partidos})

def unirse_partido(request, partido_id):
    partido = get_object_or_404(Partido, id=partido_id)
    if partido.cupos_inscritos < partido.cupos_max:
        partido.cupos_inscritos += 1
        partido.save()
    return redirect('home')