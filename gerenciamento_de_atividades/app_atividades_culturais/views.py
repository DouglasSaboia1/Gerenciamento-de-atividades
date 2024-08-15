from django.shortcuts import render, get_object_or_404, redirect
from .models import EventoCultural
from .forms import EventoCulturalForm


def home(request):
    return render(request,'home.html')

def lista_eventos(request):
    eventos = EventoCultural.objects.all().order_by('data_inicio')
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def detalhe_evento(request, pk):
    evento = get_object_or_404(EventoCultural, pk=pk)
    return render(request, 'detalhe_evento.html', {'evento': evento})


def criar_evento(request):
    if request.method == 'POST':
        form = EventoCulturalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoCulturalForm()
    
    return render(request, 'evento_form.html', {'form': form})


def editar_evento(request, pk):
    evento = get_object_or_404(EventoCultural, pk=pk)
    if request.method == 'POST':
        form = EventoCulturalForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('detalhe_evento', pk=evento.pk)
    else:
        form = EventoCulturalForm(instance=evento)
    
    return render(request, 'evento_form.html', {'form': form})