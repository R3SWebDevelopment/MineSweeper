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


class GameBoardSerializer(serializers.Serializer):
    yours = serializers.SerializerMethodField(read_only=True)
    others = serializers.SerializerMethodField(read_only=True)

    def get_yours(self, obj):
        user = get_current_user()
        qs = Game.objects.filter(players__pk=user.pk)
        return GameSerializer(qs, many=True).data

    def get_others(self, obj):
        user = get_current_user()
        qs = Game.objects.exclude(players__pk=user.pk)
        return GameSerializer(qs, many=True).data


class GameCreationSerializer(GameSerializer):
    columns = serializers.IntegerField(write_only=True, required=False)
    rows = serializers.IntegerField(write_only=True, required=False)
    mines = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Game
        fields = ('id', 'is_your_turn', 'matrix', 'marks_left', 'mines_count', 'rows', 'columns', 'time_elapsed',
                  'players', 'turn', 'columns', 'rows', 'mines', 'result', 'status', 'cells')
        read_only_fields = ('id', 'marks_left', 'mines_count', 'rows', 'columns', 'time_elapsed', 'players', 'turn',
                            'result', 'status', 'cells')

    def creation(self):
        columns = self.validated_data.get('columns', None)
        rows = self.validated_data.get('rows', None)
        mines = self.validated_data.get('mines', None)
        Game.create(get_current_user(), rows=rows, columns=columns, mines=mines)


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
        x = self.validated_data.get('x')
        y = self.validated_data.get('y')
        self.instance.mark_cell(get_current_user(), x, y)

    def unmark(self):
        x = self.validated_data.get('x')
        y = self.validated_data.get('y')
        self.instance.unmark_cell(get_current_user(), x, y)

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
