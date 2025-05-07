from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .models import Choice, Quiz


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user, "#############")
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("home")
        else:
            messages.error(request, "Registration failed. Please try again.")
    else:
        form = UserCreationForm()

    return render(request, "quiz/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            next_page = request.GET.get("next", "home")
            return redirect(next_page)
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "quiz/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, "quiz/quiz_list.html", {"quizzes": quizzes})


@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.question_set.all()

    if request.method == "POST":
        score = 0
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected:
                choice = Choice.objects.get(pk=selected)
                if choice.is_correct:
                    score += 1
        return render(
            request,
            "quiz/result.html",
            {"quiz": quiz, "score": score, "total": len(questions)},
        )

    return render(
        request, "quiz/take_quiz.html", {"quiz": quiz, "questions": questions}
    )


@login_required
def home(request):
    quiz = Quiz.objects.all()
    return render(request, "quiz/home.html", {"quiz": quiz})
