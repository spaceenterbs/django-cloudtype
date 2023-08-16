from django.urls import path
from .views import Bigreviews

urlpatterns = [
    path("", Bigreviews.as_view(), name="bigreviews"),
    path("<int:pk>/", Bigreviews.as_view(), name="bigreview_detail"),
]
