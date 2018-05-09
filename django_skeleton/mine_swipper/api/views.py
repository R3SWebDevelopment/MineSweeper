from rest_framework import viewsets
from .serializers import GameSerializer
from ..models import Game
from rest_framework.permissions import AllowAny
from crum import get_current_user


class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['post', 'get']

    def get_player(self):
        return get_current_user()

    def get_queryset(self):
        qs = super(GameViewSet, self).get_queryset()
        player = self.get_player()
        return qs.filter(players__pk=player.pk)


