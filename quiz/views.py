from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from quiz.forms import StyledUserCreationForm

from .models import AssignedQuiz, Choice, Quiz


def register(request):
    if request.method == "POST":
        form = StyledUserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("home")
        else:
            messages.error(
                request, "Registration failed. Please correct the errors below."
            )
    else:
        form = StyledUserCreationForm()

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
    django_logout(request)
    return redirect("login")


@login_required
def quiz_list(request):
    quizzes = Quiz.objects.filter(assignedquiz__user=request.user)
    return render(
        request,
        "quiz/quiz_list.html",
        {
            "quizzes": quizzes,
        },
    )


@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id, assignedquiz__user=request.user)
    questions = quiz.question_set.all()

    if request.method == "POST":
        score = 0
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected:
                choice = Choice.objects.get(pk=selected)
                if choice.is_correct:
                    score += 1

        # Update AssignedQuiz with score and mark as completed
        assigned_quiz = AssignedQuiz.objects.get(user=request.user, quiz=quiz)
        assigned_quiz.score = score
        assigned_quiz.completed = True
        assigned_quiz.save()

        return render(
            request,
            "quiz/result.html",
            {
                "quiz": quiz,
                "score": score,
                "total": len(questions),
            },
        )

    return render(
        request, "quiz/take_quiz.html", {"quiz": quiz, "questions": questions}
    )


@login_required
def leaderboard(request):
    leaderboard = (
        AssignedQuiz.objects.filter(completed=True)
        .select_related("user")
        .values("user__username", "quiz__title")
        .annotate(total_score=Sum("score"))
        .order_by("-total_score")[:10]
    )
    return render(request, "quiz/leaderboard.html", {"leaderboard": leaderboard})


@login_required
def home(request):
    quizzes = Quiz.objects.all()
    return render(request, "quiz/home.html", {"quizzes": quizzes})


@login_required
def users(request):
    users = User.objects.all()
    return render(request, "quiz/users.html", {"users": users})


@login_required
def assign_quiz_view(request):
    users = User.objects.all()
    quizzes = Quiz.objects.all()

    if request.method == "POST":
        user_id = request.POST.get("user_id")
        quiz_id = request.POST.get("quiz_id")

        if user_id and quiz_id:
            AssignedQuiz.objects.get_or_create(user_id=user_id, quiz_id=quiz_id)
        return redirect("assign_quiz")

    assignments = AssignedQuiz.objects.select_related("user", "quiz")
    return render(
        request,
        "quiz/assign_quiz.html",
        {
            "users": users,
            "quizzes": quizzes,
            "assignments": assignments,
        },
    )
