from django.db import models

class UserAnswer(models.Model):
    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)
    answer4 = models.CharField(max_length=255)
    answer5 = models.CharField(max_length=255)
    answer6 = models.CharField(max_length=255)
    answer7 = models.CharField(max_length=255)
    answer8 = models.CharField(max_length=255)
    answer9 = models.CharField(max_length=255)
    answer10 = models.CharField(max_length=255)
    answer11 = models.CharField(max_length=255)  # Add this field for Q11

    def __str__(self):
        return self.answer1  # Change this to display a meaningful representation
