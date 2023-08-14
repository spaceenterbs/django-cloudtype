from django.urls import path
from . import views

urlpatterns = [
    path("", views.Boards.as_view()),
    path("<int:pk>/", views.BoardDetail.as_view()),
]
