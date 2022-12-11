from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.
class SignUpView(View):
    def get(self, request):
        return render(request, "accounts/signup.html")

    def post(self, request):
        has_error = False
        error_string = ""
        data = request.POST
        password = data.get('password')
        password_confirm = data.get('password_confirm')
        username = data.get('username')
        if not password or not password_confirm:
            error_string += " Bad password(s)!"
            has_error = True
        if password_confirm != password:
            error_string += " Passwords don't match!"
            has_error = True
        if has_error:
            return render(request, "accounts/signup.html", {"error": error_string, "username": username})


class SignInView(View):
    def get(self, request):
        pass

def index(request):
    return render(request, "accounts/index.html")