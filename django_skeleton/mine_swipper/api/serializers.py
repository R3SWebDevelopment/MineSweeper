from rest_framework import serializers
from users.api.serializers import GamePlayerSerializer
from ..models import Game
from crum import get_current_user


class GameSerializer(serializers.ModelSerializer):
    is_your_turn = serializers.SerializerMethodField(read_only=True)
    matrix = serializers.SerializerMethodField(read_only=True)
    players = GamePlayerSerializer(many=True)
    turn = GamePlayerSerializer()

    class Meta:
        model = Game
        fields = ('id', 'is_your_turn', 'matrix', 'marks_left', 'mines_count', 'rows', 'columns', 'time_elapsed',
                  'players', 'turn', 'result', 'status')
        read_only_fields = ('id', 'marks_left', 'mines_count', 'rows', 'columns', 'time_elapsed', 'players', 'turn',
                            'result', 'status')

    def get_is_your_turn(self, obj):
        player = get_current_user()
        return obj.is_your_turn(player)

    def get_matrix(self, obj):
        return obj.cells_simple_matrix


class GameInputSerializer(GameSerializer):
    x = serializers.IntegerField(write_only=True, required=True)
    y = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = Game
        fields = ('id', 'is_your_turn', 'matrix', 'marks_left', 'mines_count', 'rows', 'columns', 'time_elapsed',
                  'players', 'turn', 'x', 'y', 'result', 'status')
        read_only_fields = ('id', 'marks_left', 'mines_count', 'rows', 'columns', 'time_elapsed', 'players', 'turn',
                            'result', 'status')

    def mark(self):
        pass

    def unmark(self):
        pass

    def reveals(self):
        pass


class GameStatusSerializer(GameSerializer):

    class Meta:
        model = Game
        fields = ('id', 'is_your_turn', 'matrix', 'marks_left', 'mines_count', 'rows', 'columns', 'time_elapsed',
                  'players', 'turn', 'result', 'status')
        read_only_fields = ('id', 'marks_left', 'mines_count', 'rows', 'columns', 'time_elapsed', 'players', 'turn',
                            'result', 'status')

    def pause(self):
        pass

    def resume(self):
        pass

    def restart(self):
        self.instance.restart(get_current_user())
