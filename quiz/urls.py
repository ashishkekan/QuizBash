from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("home/", views.home, name="home"),
    path("", views.quiz_list, name="quiz_list"),
    path("<int:quiz_id>/", views.take_quiz, name="take_quiz"),
]
