from django.urls import path

from quiz import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("home/", views.home, name="home"),
    path("users/", views.users, name="users"),
    path("quizzes/", views.quiz_list, name="quiz_list"),
    path("<int:quiz_id>/", views.take_quiz, name="take_quiz"),
    path("assign/", views.assign_quiz_view, name="assign_quiz"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
]
