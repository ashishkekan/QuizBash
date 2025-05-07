from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import QuestionForm
from .models import Choice, Question, Quiz


def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, "quiz/quiz_list.html", {"quizzes": quizzes})


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
