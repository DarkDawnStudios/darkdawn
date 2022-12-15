from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signup-weak/", views.signup_week_password, name="signup_weak"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("", views.index, name="index"),
    path('logout/', views.logout, name='logout'),
    path('recover/', views.recover, name='recover'),
]
