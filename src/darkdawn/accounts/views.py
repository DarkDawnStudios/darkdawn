import time

from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth import logout as logout_user
from django.shortcuts import redirect, render, reverse
from django.views.generic.base import View

from accounts.utils import check_password

user_model = get_user_model()


# Create your views here.
class SignUpView(View):
    def get(self, request):
        return render(request, "accounts/signup.html")

    def post(self, request):
        error_string = ""
        data = request.POST
        username = data.get("username")
        if len(username) < 4:
            error_string += " The minimum length of a username is 4."
        user = user_model.objects.filter(username=username).first()
        if user is not None:
            error_string += " This username is taken."
        password = data.get("password")
        password_confirm = data.get("password_confirm")
        if not password or not password_confirm:
            error_string += " Bad password(s)."
        if password_confirm != password:
            error_string += " Passwords don't match."
        if error_string:
            return render(
                request,
                "accounts/signup.html",
                {"error": error_string, "username": username},
            )
        if check_password(password) is False:
            return render(
                request,
                "accounts/weak_password.html",
                {"username": username, "password": password},
            )
        user = user_model.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect(reverse("core:index"))


def signup_weak_password(request):
    data = request.POST
    username = data.get("username")
    password = data.get("password")
    error_string = ""
    if len(username) < 4:
        error_string += " Your username is too short (< 4 characters)"
    user = user_model.objects.filter(username=username).first()
    if user is not None:
        error_string += " This username is taken!"
    if error_string:
        return render(request, "accounts/weak_password.html", {"error": error_string})
    user = user_model.objects.create_user(username=username, password=password)
    login(request, user)
    return redirect(reverse("core:index"))


class SignInView(View):
    def get(self, request):
        return render(request, "accounts/signin.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if not user or user.is_authenticated is False:
            time.sleep(1)
            return render(
                request,
                "accounts/signin.html",
                {"error": "Bad credentials.", "username": username},
            )
        login(request, user)
        return redirect(reverse("core:index"))


def logout(request):
    logout_user(request)
    return redirect(reverse("core:index"))


def index(request):
    return render(request, "accounts/index.html")


def recover(request):
    return render(request, "accounts/recover.html")


class ResetPasswordView(View):
    def get(self, request):
        return render(request, "accounts/reset_password.html")

    def post(self, request):
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        user = request.user
        is_old_pwd_correct = user.check_password(old_password)
        if not is_old_pwd_correct:
            return render(
                request,
                "accounts/reset_password.html",
                {"error": "The old password is wrong."},
            )
        is_new_password_safe = check_password(new_password)
        if is_new_password_safe:
            user.set_password(new_password)
            user.save()
        else:
            return render(request, "accounts/weak_password.html", {"is_reset": True})
        return redirect(reverse("core:index"))


def reset_weak_password(request):
    user = request.user
    password = request.POST.get("password")
    if not password:
        return render(
            request,
            "accounts/weak_password.html",
            {"is_reset": True, "error": "Empty password!"},
        )
    user.set_password(password)
    return render(
        request,
        "accounts/reset_password.html",
        {"message": "Your password reset is done."},
    )
