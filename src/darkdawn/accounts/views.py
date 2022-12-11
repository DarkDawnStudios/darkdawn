from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.
class SignUpView(View):
    def get(self, request):
        return render(request, "accounts/signup.html")

    def post(self, request):
        error_string = ""
        data = request.POST
        username = data.get('username')
        if not username:
            error_string += "Empty username."
        password = data.get('password')
        password_confirm = data.get('password_confirm')
        if not password or not password_confirm:
            error_string += " Bad password(s)."
        if password_confirm != password:
            error_string += " Passwords don't match."
        if error_string:
            return render(request, "accounts/signup.html", {"error": error_string, "username": username})


class SignInView(View):
    def get(self, request):
        pass

def index(request):
    return render(request, "accounts/index.html")