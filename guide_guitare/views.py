from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import GuitareForm
from .models import GuitareModel
from .models import TYPE_GUITARE_CHOICES


def index(request):
    items = GuitareModel.objects.all()
    for item in items:
        item.type_guitare = TYPE_GUITARE_CHOICES[int(item.type_guitare) - 1][1]
    return render(request, 'guide_guitare/index.html', {"items": items})


def create_guitare(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = GuitareForm(request.POST, request.FILES)
            print(form.is_valid())
            if form.is_valid():
                form.save()
                return redirect(index)
        else:
            form = GuitareForm()
    else:
        return redirect(connexion)
    return render(request, 'guide_guitare/create_guitares.html', {"form": form})


def guitares(request, id_guitare):
    try:
        item = GuitareModel.objects.get(id=id_guitare)
    except GuitareModel.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = GuitareForm(request.POST, request.FILES, instance=item)
        if form.is_valid() and 'modifier' in request.POST:
            form.save()
            return redirect(index)
        elif 'supprimer' in request.POST:
            item.delete()
            return redirect(index)
    else:
        form = GuitareForm(instance=item)

    return render(request, 'guide_guitare/guitares.html', {"item": item, 'form': form})


def connexion(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(index)
    return render(request, 'guide_guitare/connexion.html')


def logout_view(request):
    logout(request)
    return redirect(index)
