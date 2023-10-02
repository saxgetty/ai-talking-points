from django.urls import path
from . import views

urlpatterns = [
    path('generateTalkingPoints/', views.generateTalkingPoints, name='generateTalkingPoints'),
]
