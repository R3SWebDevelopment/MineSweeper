from rest_framework import viewsets
from .serializers import GameSerializer
from ..models import Game
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = (AllowAny,)

    def get_player(self):
        return User.objects.get(pk=1)

    def get_queryset(self):
        qs = super(GameViewSet, self).get_queryset()
        player = self.get_player()
        return qs.filter(players__pk=player.pk)


