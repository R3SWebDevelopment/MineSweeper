from rest_framework import viewsets
from .serializers import GameSerializer, GameInputSerializer, GameStatusSerializer, GameBoardSerializer, \
    GameCreationSerializer
from ..models import Game
from rest_framework.permissions import IsAuthenticated
from crum import get_current_user
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.action in ['create', 'retrieve', 'list']:
            return self.serializer_class
        elif self.action in ['mark', 'reveals', 'unmark']:
            return GameInputSerializer
        elif self.action in ['pause', 'restart', 'resume', 'join', 'leave']:
            return GameStatusSerializer
        elif self.action in ['creation', ]:
            return GameCreationSerializer
        return self.serializer_class

    def get_player(self):
        return get_current_user()

    def get_queryset(self):
        qs = super(GameViewSet, self).get_queryset()
        player = self.get_player()
        return qs

    @action(methods=['post'], detail=False)
    def creation(self, request):
        """
        Create a new game
        """
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.creation()
            serializer = GameBoardSerializer({})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False)
    def board(self, request):
        """
        Returns the game boar list
        """
        serializer = GameBoardSerializer({})
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def reveals(self, request, pk=None):
        """
        Reveal the cell on position x and y
        """
        game = self.get_object()
        serializer = self.get_serializer_class()(game, data=request.data)
        if serializer.is_valid():
            serializer.reveals()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def mark(self, request, pk=None):
        """
        Mark the cell on position x and y
        """
        game = self.get_object()
        serializer = self.get_serializer_class()(game, data=request.data)
        if serializer.is_valid():
            serializer.mark()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def unmark(self, request, pk=None):
        """
        Unmark the cell on position x and y
        """
        game = self.get_object()
        serializer = self.get_serializer_class()(game, data=request.data)
        if serializer.is_valid():
            serializer.unmark()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def pause(self, request, pk=None):
        """
        Pause the game
        """
        game = self.get_object()
        serializer = self.get_serializer_class()(game, data=request.data)
        if serializer.is_valid():
            serializer.pause()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def join(self, request, pk=None):
        """
        Join the game
        """
        game = self.get_object()
        serializer = self.get_serializer_class()(game, data=request.data)
        if serializer.is_valid():
            serializer.join()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def leave(self, request, pk=None):
        """
        Leave the game
        """
        game = self.get_object()
        serializer = self.get_serializer_class()(game, data=request.data)
        if serializer.is_valid():
            serializer.leave()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def resume(self, request, pk=None):
        """
        Resume the game
        """
        game = self.get_object()
        serializer = self.get_serializer_class()(game, data=request.data)
        if serializer.is_valid():
            serializer.resume()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def restart(self, request, pk=None):
        """
        Restart the game
        """
        game = self.get_object()
        serializer = self.get_serializer_class()(game, data=request.data)
        if serializer.is_valid():
            serializer.restart()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


