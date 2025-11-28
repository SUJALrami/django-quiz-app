from django.contrib import admin
from .models import Event, Quiz, Question, Answer, UserSubmission

# Allow adding Answers directly when creating a Question
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4  # Show 4 blank answer slots by default

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

# Allow adding Questions directly when creating a Quiz
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Event)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(UserSubmission)