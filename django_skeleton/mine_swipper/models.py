from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField, JSONField
from django.utils.translation import ugettext as _

DEFAULT_CELLS = 10
MIN_CELLS = 10
MAX_CELLS = 30
DEFAULT_MINES = 10
MIN_MINES = 10
MAX_MINES = 30

GAME_STARTED = 1
GAME_PAUSED = 2
GAME_LOST = 3
GAME_WON = 4

GAME_STATUS = (
    (GAME_STARTED, _('Started')),
    (GAME_PAUSED, _('Paused')),
    (GAME_LOST, _('Lost')),
    (GAME_WON, _('Won')),
)


class Game(models.Model):
    rows = models.IntegerField(null=False, default=DEFAULT_CELLS, validators=[
            MaxValueValidator(MAX_CELLS),
            MinValueValidator(MIN_CELLS)
        ])
    columns = models.IntegerField(null=False, default=DEFAULT_CELLS, validators=[
            MaxValueValidator(MAX_CELLS),
            MinValueValidator(MIN_CELLS)
        ])
    mines_count = models.IntegerField(null=False, default=DEFAULT_MINES, validators=[
            MaxValueValidator(MAX_MINES),
            MinValueValidator(MIN_MINES)
        ])
    mines_left = models.IntegerField(null=False, default=0)
    cells = ArrayField(ArrayField(JSONField()))
    flags = ArrayField(ArrayField(JSONField()))
    payers = models.ManyToManyField(User, related_name="games")
    turn = models.ForeignKey(User, related_name="current_move", null=True, default=None)
    status = models.IntegerField(null=False, default=DEFAULT_MINES, choices=GAME_STATUS)
    seconds = models.IntegerField(null=False, default=0)
    started_timestamp = models.DateTimeField(null=False, auto_now_add=True)
    last_turn = models.ForeignKey(User, related_name="last_move", null=True, default=None)

    def __str__(self):
        return "Game"
