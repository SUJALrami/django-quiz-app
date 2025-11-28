from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Quiz, Question, Answer, UserSubmission, UserAnswer

def home(request):
    return render(request, 'core/home.html')

def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'core/event_list.html', {'events': events})

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'core/quiz_list.html', {'quizzes': quizzes})

def quiz_attempt(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        score = 0
        total_questions = quiz.questions.count()
        
        # Create the submission container first
        submission = UserSubmission.objects.create(
            quiz=quiz,
            user_name=user_name,
            score=0 
        )

        # Loop through questions to check answers
        for question in quiz.questions.all():
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                selected_answer = Answer.objects.get(id=selected_answer_id)
                is_correct = selected_answer.is_correct
                
                if is_correct:
                    score += 1
                
                # Save the user's answer
                UserAnswer.objects.create(
                    submission=submission,
                    question=question,
                    answer=selected_answer,
                    is_correct=is_correct
                )
        
        # Update final score
        submission.score = score
        submission.save()
        
        return redirect('quiz_result', submission_id=submission.id)

    return render(request, 'core/quiz_attempt.html', {'quiz': quiz})

def quiz_result(request, submission_id):
    submission = get_object_or_404(UserSubmission, id=submission_id)
    total_questions = submission.quiz.questions.count()
    percentage = (submission.score / total_questions) * 100 if total_questions > 0 else 0
    
    context = {
        'submission': submission,
        'total_questions': total_questions,
        'percentage': round(percentage, 2)
    }
    return render(request, 'core/quiz_result.html', context)