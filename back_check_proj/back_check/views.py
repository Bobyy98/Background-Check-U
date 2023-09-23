# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import UserAnswer

# Show the background check form
def show_background_check_form(request):
    return render(request, 'back_check/index.html')

# Show the second page (index2.html)
def show_second_page(request):
    return render(request, 'back_check/index2.html')

# Process the background check form
def process_background_check_form(request):
    if request.method == 'POST':
        # Retrieve data from the submitted form
        answer1 = request.POST.get('answer1')
        answer2 = request.POST.get('answer2')
        answer3 = request.POST.get('answer3')
        answer4 = request.POST.get('answer4')
        answer5 = request.POST.get('answer5')
        answer6 = request.POST.get('answer6')
        answer7 = request.POST.get('answer7')
        answer8 = request.POST.get('answer8')
        answer9 = request.POST.get('answer9')
        answer10 = request.POST.get('answer10')
        answer11 = request.POST.get('incomeOptions')  # Rename this variable for clarity

        # Calculate average score (you can do this here if needed)
        avg_score = (int(answer1) + int(answer2) + int(answer3) + int(answer4) + int(answer5) +
                     int(answer6) + int(answer7) + int(answer8) + int(answer9) + int(answer10)) / 100

        # Save the data to the database using your model
        UserAnswer.objects.create(
            answer1=answer1,
            answer2=answer2,
            answer3=answer3,
            answer4=answer4,
            answer5=answer5,
            answer6=answer6,
            answer7=answer7,
            answer8=answer8,
            answer9=answer9,
            answer10=answer10,
            answer11=answer11  # Save the answer of Q11
        )

        # Redirect to the Thank You page with the average score
        thank_you_url = reverse('thank_you')  # Generate the URL for the 'thank_you' view
        return redirect(thank_you_url)  # Redirect to the Thank You page

# Thank You page
def thank_you(request):
    # Fetch the last data entry from the database
    latest_answer = UserAnswer.objects.latest('id')

    # Calculate the average score based on the last entry
    avg_score = (
        int(latest_answer.answer1) + int(latest_answer.answer2) +
        int(latest_answer.answer3) + int(latest_answer.answer4) +
        int(latest_answer.answer5) + int(latest_answer.answer6) +
        int(latest_answer.answer7) + int(latest_answer.answer8) +
        int(latest_answer.answer9) + int(latest_answer.answer10)
    ) / 100

    # Pass the average score to the template
    context = {'avg_score': avg_score}
    return render(request, 'back_check/thank_you.html', context)