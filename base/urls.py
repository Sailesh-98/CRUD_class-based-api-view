from django.urls import path
from base import views

urlpatterns = [

    path('studentapi/', views.studentAPI.as_view()),
    path('studentapi/<int:pk>/', views.studentAPI.as_view()),
]