from django.contrib import admin
from django.urls import path
from back_check import views  # Import your app's views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('process-background-check/', views.process_background_check_form, name='process_background_check'),
    path('', views.show_background_check_form, name='background_check_form'),
    path('back_check/index2.html/', views.show_second_page, name='second_page'),  # Add this line
    path('thank-you/', views.thank_you, name='thank_you'),
]
