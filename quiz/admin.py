from django.contrib import admin

from .models import Choice, Question, Quiz

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
