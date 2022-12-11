from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import get_user_model
from accounts.utils import check_password

user_model = get_user_model()


# Create your views here.
class SignUpView(View):
    def get(self, request):
        return render(request, "accounts/signup.html")

    def post(self, request):
        error_string = ""
        data = request.POST
        username = data.get('username')
        if len(username) < 4:
            error_string += " The minimum length of a username is 4."
        user = user_model.objects.filter(username=username).first()
        if user is not None:
            error_string += " This username is taken."
        password = data.get('password')
        password_confirm = data.get('password_confirm')
        if not password or not password_confirm:
            error_string += " Bad password(s)."
        if password_confirm != password:
            error_string += " Passwords don't match."
        if error_string:
            return render(request, "accounts/signup.html", {"error": error_string, "username": username})
        if check_password(password) is False:
            ...
        else:
            ...

class SignInView(View):
    def get(self, request):
        pass

def index(request):
    return render(request, "accounts/index.html")