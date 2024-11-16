from django.shortcuts import render


def index(request):
    return render(request, "base.html")


def notespage(request):
    return render(request, "makenotes.html")


# Create your views here.
