from rest_framework import viewsets
from .serializers import GameSerializer, GameInputSerializer
from ..models import Game
from rest_framework.permissions import AllowAny
from crum import get_current_user
from rest_framework.decorators import action
from rest_framework.response import Response


class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.action in ['create']:
            return self.serializer_class
        elif self.action in ['mark', 'reveals', 'unmark']:
            return GameInputSerializer
        elif self.action in ['pause', 'restart', 'resume']:
            pass
        return self.serializer_class

    def get_player(self):
        return get_current_user()

    def get_queryset(self):
        qs = super(GameViewSet, self).get_queryset()
        player = self.get_player()
        return qs.filter(players__pk=player.pk)


