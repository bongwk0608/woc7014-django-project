from django.urls import path
from .views import GameReviewListView

urlpatterns = [
    path('reviews/', GameReviewListView.as_view(), name='review-list'),
]