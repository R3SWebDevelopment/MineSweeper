from rest_framework import serializers
from ..models import Game
from crum import get_current_user


class GameSerializer(serializers.ModelSerializer):
    is_your_turn = serializers.SerializerMethodField(read_only=True)
    matrix = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'is_your_turn', 'matrix')

    def get_is_your_turn(self, obj):
        player = get_current_user()
        return obj.turn == player

    def get_matrix(self, obj):
        return obj.cells_simple_matrix


class GameInputSerializer(GameSerializer):
    x = serializers.IntegerField(write_only=True, required=True)
    y = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = Game
        fields = ('id', 'is_your_turn', 'x', 'y')

    def mark(self):
        pass

    def unmark(self):
        pass

    def reveals(self):
        pass


class GameStatusSerializer(GameSerializer):

    class Meta:
        model = Game
        fields = ('id', 'is_your_turn')

    def pause(self):
        pass

    def resume(self):
        pass

    def restart(self):
        pass
