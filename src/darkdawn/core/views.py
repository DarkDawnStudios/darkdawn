from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def ping(request):
    return HttpResponse()


def index(request):
    return render(request, "core/index.html")