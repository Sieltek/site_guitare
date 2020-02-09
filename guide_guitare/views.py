from django.http import Http404
from django.shortcuts import render, redirect

from .forms import GuitareForm
from .models import GuitareModel
from .models import TYPE_GUITARE_CHOICES


def index(request):
    items = GuitareModel.objects.all()
    for item in items:
        item.type_guitare = TYPE_GUITARE_CHOICES[int(item.type_guitare) - 1][1]
    return render(request, 'guide_guitare/index.html', {"items": items})


def create_guitare(request):
    if request.method == 'POST':
        form = GuitareForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = GuitareForm()
    return render(request, 'guide_guitare/create_guitares.html', {"form": form})


def guitares(request, id_guitare):
    try:
        item = GuitareModel.objects.get(id=id_guitare)
    except GuitareModel.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = GuitareForm(request.POST, request.FILES, instance=item)
        print(form.is_valid())
        if form.is_valid() and 'modifier' in request.POST:
            form.save()
            return redirect(index)
        elif 'supprimer' in request.POST:
            item.delete()
            return redirect(index)
    else:
        form = GuitareForm(instance=item)

    return render(request, 'guide_guitare/guitares.html', {"item": item, 'form': form})
