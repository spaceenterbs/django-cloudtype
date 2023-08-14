from django.urls import path
from . import views

# from .views import CountResult

urlpatterns = [
    path("", views.Bigreviews.as_view()),
    # path("<int:pk>/", views.Youtube_VideoDetail.as_view()),
]
