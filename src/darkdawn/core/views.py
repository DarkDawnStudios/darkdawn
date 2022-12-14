from django.http import HttpResponse
from django.shortcuts import render
from ipware import get_client_ip


# Create your views here.
def ping(request):
    ip, _ = get_client_ip(request)
    return HttpResponse(f"Pinged from {ip}")


def index(request):
    return render(request, "core/index.html")
