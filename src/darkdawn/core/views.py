from django.http import HttpResponse
from django.shortcuts import redirect, render
from ipware import get_client_ip


# Create your views here.
def ping(request):
    ip, _ = get_client_ip(request)
    return HttpResponse(f"Pinged by {ip}")


def index(request):
    return render(request, "core/index.html")
