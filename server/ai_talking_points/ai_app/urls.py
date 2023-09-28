from django.urls import path
from . import views

urlpatterns = [
    path('generateTalkingPoints/', views.generate_talking_points, name='generate_talking_points'),
]