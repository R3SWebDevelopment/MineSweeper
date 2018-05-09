from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField, JSONField
from django.utils.translation import ugettext as _
import random
import json
import datetime

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
    mines = ArrayField(ArrayField((models.IntegerField())), null=True)
    cells = ArrayField(ArrayField(models.TextField(null=False)), null=True)
    flags = ArrayField(ArrayField(models.TextField(null=False)), null=True)
    players = models.ManyToManyField(User, related_name="games")
    turn = models.ForeignKey(User, related_name="current_move", null=True, default=None)
    status = models.IntegerField(null=False, default=GAME_STARTED, choices=GAME_STATUS)
    seconds = models.IntegerField(null=False, default=0)
    started_timestamp = models.DateTimeField(null=False, auto_now_add=True)
    last_turn = models.ForeignKey(User, related_name="last_move", null=True, default=None)

    def __str__(self):
        return "Game"

    @classmethod
    def create(cls, user, rows=None, columns=None, mines=None):
        """
        Creates a new instance of the game if any of the parameters (rows, columns or mines) are null,
        the class randomly assign a value within the max and min values
        """
        rows = random.randint(MIN_MINES, MAX_MINES) if rows is None else rows
        columns = random.randint(MIN_MINES, MAX_MINES) if columns is None else columns
        mines = random.randint(MIN_MINES, MAX_MINES) if mines is None else mines
        game = cls.objects.create(turn=user, rows=rows, columns=columns, mines_count=mines)
        game.players.add(user)
        game.build_cells()
        return game

    def cell_has_boom(self, x, y):
        """
        Checks if the cell on x and y coordinates there is a boom
        """
        return [x, y] in self.mines

    @property
    def get_seconds(self):
        """
        Get the seconds of the game
        """
        seconds = self.seconds
        if self.status in [GAME_STARTED]:
            delta = datetime.datetime.now() - self.started_timestamp.replace(tzinfo=None)
            seconds += delta.seconds
        return seconds

    def cell(self, x, y):
        """
        Returns the data of the cell
        """
        if x >= self.columns:
            raise ValueError(_('Out of range column'))
        if y >= self.rows:
            raise ValueError(_('Out of range row'))
        cell = self.cells[x][y]
        return json.loads(cell)

    def set_cell(self, x, y, data, save=True):
        """
        Set the data on a cell
        """
        if x >= self.columns:
            raise ValueError(_('Out of range column'))
        if y >= self.rows:
            raise ValueError(_('Out of range row'))
        self.cells[x][y] = json.dumps(data)
        if save:
            self.save()

    def build_cells(self):
        """
        Builds the cells for the game using the rows, columns and mines parameters
        """
        def get_adjacent(x, y, mines):
            adjacents = []
            if x == 0 and y == 0:
                adjacents = [(0, 1), (1, 0), (1, 1)]
            elif x == 0 and y == self.rows - 1:
                adjacents = [(0, self.rows - 2), (1, self.columns - 1), (1, self.rows - 2)]
            elif x == self.columns - 1 and y == 0:
                adjacents = [(self.columns - 2, 0), (self.columns - 2, 1), (self.columns - 1, 1)]
            elif x == self.columns - 1 and y == self.rows - 1:
                adjacents = [(self.columns - 2, self.rows - 2), (self.columns - 2, self.rows - 1),
                             (self.columns - 1, self.rows - 2)]
            elif y == 0:
                adjacents = [(x - 1, 0), (x - 1, 1), (x, 1), (x + 1, 0), (x + 1, 1)]
            elif y == self.rows - 1:
                adjacents = [(x - 1, self.rows - 1), (x - 1, self.rows - 2), (x, self.rows - 2),
                             (x + 1, self.rows - 1), (x + 1, self.rows - 2)]
            elif x == 0:
                adjacents = [(x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y + 1)]
            elif x == self.columns - 1:
                adjacents = [(x, y - 1), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1)]
            else:
                adjacents = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x + 1, y + 1),
                             (x, y + 1), (x + 1, y + 1)]
            return adjacents

        def get_adjacents_count(adjacents, mines):
            count = 0
            for position in adjacents:
                if position in mines:
                    count += 1
            return count

        mines = []
        for _ in range(0, self.mines_count):
            x = random.randint(0, self.columns - 1)
            y = random.randint(0, self.rows - 1)
            while (x, y) in mines:  # Verify that the position of the boom is not already defined
                x = random.randint(0, self.columns - 1)
                y = random.randint(0, self.rows - 1)
            mines.append((x, y))
        cells = []
        for x in range(0, self.columns - 1):
            rows = []
            for y in range(0, self.rows - 1):
                adjacents = get_adjacent(x, y, mines)
                rows.append(json.dumps({
                    "is_marked": False,
                    "is_reveal": False,
                    "has_boom": None,
                    "count": get_adjacents_count(adjacents, mines),
                    "adjacents": adjacents,
                }))
            cells.append(rows)
        self.cells = cells
        self.mines = [list(p) for p in mines]
        self.save()

    def join(self, user):
        """
        Adds the user to the list of users playing the game
        """
        self.players.add(user)

    def leave(self, user):
        """
        Removes the user from the list of users playing the game
        """
        self.players.remove(user)

    def mark_cell(self, user, x, y):
        """
        Marks the given cell on x and y to be a possible cell with boom
        """
        if self.status not in [GAME_STARTED]:
            raise Exception(_('The game is not started'))
        cell = self.cell(x, y)
        if cell.get('is_marked', False):
            raise Exception(_('This cell is already marked'))
        cell.update({
            "is_marked": True
        })
        self.set_cell(x, y, cell)

    def unmark_cell(self, user, x, y):
        """
        Unmarks the given cell on x and y to be a possible cell with boom
        """
        if self.status not in [GAME_STARTED]:
            raise Exception(_('The game is not started'))
        cell = self.cell(x, y)
        if not cell.get('is_marked', False):
            raise Exception(_('This cell is not marked'))
        cell.update({
            "is_marked": False
        })
        self.set_cell(x, y, cell)

    def reveal_cell(self, user, x, y, save=True):
        """
        Reveal the given cell on x and y
        """
        if self.status not in [GAME_STARTED]:
            raise Exception(_('The game is not started'))
        cell = self.cell(x, y)
        if cell.get('is_marked', False):
            raise Exception(_('This cell is marked'))
        if cell.get('is_reveal', False):
            raise Exception(_('This cell is already revealed'))
        cell.update({
            "is_reveal": True
        })
        if self.cell_has_boom(x, y):  # This cell has a boom
            cell.update({
                "has_boom": True
            })
        else:
            if cell.get('count', 0) == 0:  # This cell does not have adjacents
                self.__reveal_adjacents(cell.get('adjacents', []))
            cell.update({
                "has_boom": False
            })
        self.set_cell(x, y, cell, save=save)

    def __reveal_adjacents(self, user, adjacents=[]):
        """
        Reveals adjacents cells, this method assumes that the saving of the state on the database will be handle by the
        calling method, this method is private, also this method contains any exception that might raise due any
        validation placed on reveal_cell method, to avoid brake the process
        """
        for coordinates in adjacents:
            x = coordinates[0]
            y = coordinates[1]
            try:
                self.reveal_cell(user, x, y, save=False)
            except Exception as e:
                print("Cell ({}, {}) raises: {}".format(x, y, e))

    def pause(self, user):
        """
        Pause the time of the game to stop the timer and to prevent any user to do something on the game
        """
        if self.status not in [GAME_STARTED]:
            raise Exception(_('The game is not started'))
        self.status = GAME_PAUSED
        delta = datetime.datetime.now() - self.started_timestamp.replace(tzinfo=None)
        self.seconds += delta.seconds
        self.save()

    def resume(self, user):
        """
        Resume the time of the game to restart the timer and allow any user to do something on the game
        """
        if self.status not in [GAME_PAUSED]:
            raise Exception(_('The game is not paused'))
        self.started_timestamp = datetime.date.now()
        self.save()