from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.
class SignUpView(View):
    def get(self, request):
        return render(request, "accounts/signup.html")

    def post(self, request):
        pass


class SignInView(View):
    def get(self, request):
        pass

def index(request):
    return render(request, "accounts/index.html")