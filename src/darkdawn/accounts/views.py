from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.
class SignUpView(View):
    def get(self, request):
        return render(request, "")

    def post(self, request):
        pass


class SignInView(View):
    def get(self, request):
        pass
