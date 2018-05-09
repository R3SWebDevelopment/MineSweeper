from rest_framework import serializers
from ..models import Game
from crum import get_current_user


class GameSerializer(serializers.ModelSerializer):
    is_your_turn = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'is_your_turn')

    def get_is_your_turn(self, obj):
        player = get_current_user()
        return obj.turn == player