from django.views.generic import ListView
from .models import Review

class GameReviewListView(ListView):
    model = Review
    template_name = 'gamereview_list.html'
    context_object_name = 'reviews'