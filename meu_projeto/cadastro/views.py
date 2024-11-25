from django.shortcuts import render, get_object_or_404, redirect
from .models import FilmeSerie
from .forms import FilmeSerieForm

def criar_filme_serie(request):
    if request.method == 'POST':
        form = FilmeSerieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes_series')  # Redireciona para a listagem
    else:
        form = FilmeSerieForm()
    return render(request, 'cadastro/criar_filme_serie.html', {'form': form})


def listar_filmes_series(request):
    filmes_series = FilmeSerie.objects.all()  # Obtém todos os filmes e séries
    return render(request, 'cadastro/listar_filmes_series.html', {'filmes_series': filmes_series})


def editar_filme_serie(request, id):
    filme_serie = get_object_or_404(FilmeSerie, id=id)
    
    if request.method == 'POST':
        form = FilmeSerieForm(request.POST, request.FILES, instance=filme_serie)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes_series')  # Redireciona para a página de listagem após editar
    else:
        form = FilmeSerieForm(instance=filme_serie)
    
    return render(request, 'cadastro/editar_filme_serie.html', {'form': form})


def excluir_filme_serie(request, id):
    filme_serie = get_object_or_404(FilmeSerie, id=id)
    filme_serie.delete()
    return redirect('listar_filmes_series')  # Redireciona para a lista de filmes e séries
