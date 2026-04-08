from django.shortcuts import render
from .models import Partido


def home(request):
    partidos = Partido.objects.all()

    distrito_filtrado = request.GET.get('distrito')

    if distrito_filtrado:
        partidos = partidos.filter(lugar__icontains=distrito_filtrado)

    return render(request, 'home.html', {'partidos': partidos})