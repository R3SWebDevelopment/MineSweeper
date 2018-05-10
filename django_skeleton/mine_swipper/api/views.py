from rest_framework import viewsets
from .serializers import GameSerializer, GameInputSerializer, GameStatusSerializer
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
            return GameStatusSerializer
        return self.serializer_class

    def get_player(self):
        return get_current_user()

    def get_queryset(self):
        qs = super(GameViewSet, self).get_queryset()
        player = self.get_player()
        return qs.filter(players__pk=player.pk)

    @action(methods=['post'], detail=True)
    def reveals(self, request, pk=None):
        """
        Reveal the cell on position x and y
        """
        pass

    @action(methods=['post'], detail=True)
    def mark(self, request, pk=None):
        """
        Mark the cell on position x and y
        """
        pass

    @action(methods=['post'], detail=True)
    def unmark(self, request, pk=None):
        """
        Unmark the cell on position x and y
        """
        pass

    @action(methods=['post'], detail=True)
    def pause(self, request, pk=None):
        """
        Pause the game
        """
        pass

    @action(methods=['post'], detail=True)
    def resume(self, request, pk=None):
        """
        Resume the game
        """
        pass

    @action(methods=['post'], detail=True)
    def restart(self, request, pk=None):
        """
        Restart the game
        """
        game = self.get_object()
        serializer = self.get_serializer_class()(game)
        serializer.restart()
        return Response(serializer.data)


