from django.views import generic
from .models import Game

class GameListView(generic.ListView):
    template_name = 'gamereview/gamelist.html'
    context_object_name = 'all_games'

    def get_queryset(self):
        return Game.objects.all()


class ReviewView(generic.DetailView):
    model = Game
    template_name = 'gamereview/review.html'
    context_object_name = 'game'  # optional but nicer