from rest_framework import serializers
from users.api.serializers import GamePlayerSerializer
from ..models import Game
from crum import get_current_user


class GameSerializer(serializers.ModelSerializer):
    is_your_turn = serializers.SerializerMethodField(read_only=True)
    matrix = serializers.SerializerMethodField(read_only=True)
    cells = serializers.SerializerMethodField(read_only=True)
    players = GamePlayerSerializer(many=True, read_only=True)
    turn = GamePlayerSerializer(read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'is_your_turn', 'matrix', 'marks_left', 'mines_count', 'rows', 'columns', 'time_elapsed',
                  'players', 'turn', 'result', 'status', 'cells')
        read_only_fields = ('id', 'marks_left', 'mines_count', 'rows', 'columns', 'time_elapsed', 'players', 'turn',
                            'result', 'status', 'cells')

    def get_is_your_turn(self, obj):
        player = get_current_user()
        return obj.is_your_turn(player)

    def get_matrix(self, obj):
        return obj.cells_simple_matrix

    def get_cells(self, obj):
        return obj.cells_data


class GameInputSerializer(GameSerializer):
    x = serializers.IntegerField(write_only=True, required=True)
    y = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = Game
        fields = ('id', 'is_your_turn', 'matrix', 'marks_left', 'mines_count', 'rows', 'columns', 'time_elapsed',
                  'players', 'turn', 'x', 'y', 'result', 'status', 'cells')
        read_only_fields = ('id', 'marks_left', 'mines_count', 'rows', 'columns', 'time_elapsed', 'players', 'turn',
                            'result', 'status', 'cells')

    def mark(self):
        pass

    def unmark(self):
        pass

    def reveals(self):
        x = self.validated_data.get('x')
        y = self.validated_data.get('y')
        self.instance.reveal_cell(get_current_user(), x, y)


class GameStatusSerializer(GameSerializer):

    class Meta:
        model = Game
        fields = ('id', 'is_your_turn', 'matrix', 'marks_left', 'mines_count', 'rows', 'columns', 'time_elapsed',
                  'players', 'turn', 'result', 'status', 'cells')
        read_only_fields = ('id', 'marks_left', 'mines_count', 'rows', 'columns', 'time_elapsed', 'players', 'turn',
                            'result', 'status', 'cells')

    def pause(self):
        self.instance.pause(get_current_user())

    def resume(self):
        self.instance.resume(get_current_user())

    def restart(self):
        self.instance.restart(get_current_user())
