from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_limit = models.IntegerField(help_text="Time limit in seconds")

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
