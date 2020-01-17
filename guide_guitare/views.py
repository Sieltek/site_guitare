from django.shortcuts import render


def index(request):

    return render(request, 'guide_guitare/index.html')
