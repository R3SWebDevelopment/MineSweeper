from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField, JSONField
from django.utils.translation import ugettext as _
from django.urls import reverse
import random
import json
import datetime
import numpy as np

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
    revelead_cells = ArrayField(ArrayField((models.IntegerField())), null=True)
    marked_cells = ArrayField(ArrayField((models.IntegerField())), null=True)
    cells = ArrayField(ArrayField(models.TextField(null=False)), null=True)
    players = models.ManyToManyField(User, related_name="games")
    turn = models.ForeignKey(User, related_name="current_move", null=True, default=None)
    status = models.IntegerField(null=False, default=GAME_STARTED, choices=GAME_STATUS)
    seconds = models.IntegerField(null=False, default=0)
    started_timestamp = models.DateTimeField(null=False, auto_now_add=True)
    last_turn = models.ForeignKey(User, related_name="last_move", null=True, default=None)
    result = models.CharField(max_length=250, null=True, default="")

    def __str__(self):
        return "Game"

    @property
    def cells_data(self):
        data = {}
        for x in range(0, self.columns):
            for y in range(0, self.rows):
                cell = self.cell(x, y)
                if cell.get('is_reveal', False):  # The cell is reveal
                    if cell.get('has_boom', False):  # The cell has a boom
                        value = 'B'
                    elif cell.get('count', 0) == 0:  # The cell does not has adjacents
                        value = '_'
                    else:  # The cell does has adjacents
                        value = '{}'.format(cell.get('count', 0))
                else:
                    if cell.get('is_marked', False):  # The cell has been marked
                        value = '?'
                    else:
                        value = '*'
                data.update({
                    "{}_{}".format(x, y): value
                })
        return data

    @property
    def marks_left(self):
        return self.mines_count - self.marked_cells_count

    @property
    def marked_cells_count(self):
        return len(self.marked_cells) if self.marked_cells is not None else 0

    @property
    def reveled_cells_count(self):
        return len(self.revelead_cells) if self.revelead_cells is not None else 0

    @property
    def cells_count(self):
        return self.rows * self.columns

    @property
    def are_mines_marked(self):
        """
        Return True if all the mine cells has been marked and the only cells none revealed are the one with mines
        """
        cells_count = self.cells_count
        if (cells_count - self.reveled_cells_count) == self.mines_count and self.marks_left == 0:
            return True
        return False

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

    def is_your_turn(self, user):
        """
        Checks if the user has the turn
        """
        return self.turn == user

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

    def check_board_status(self, user):
        """
        Checks if the game is over
        """
        if self.status in [GAME_STARTED]:
            if self.are_mines_marked:
                self.finish(user, won=True)

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
        for x in range(0, self.columns):
            rows = []
            for y in range(0, self.rows):
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
        self.revelead_cells = []
        self.marked_cells = []
        self.mines = [list(p) for p in mines]
        self.save()

    def finish(self, user, boom=False, won=False, x=0, y=0):
        """
        Define the outcome of the game
        """
        if boom:
            self.result = "User: {} revealed a Mine at cell ({}, {})".format(user.get_full_name(), x, y)
            self.status = GAME_LOST
            delta = datetime.datetime.now() - self.started_timestamp.replace(tzinfo=None)
            self.seconds += delta.seconds
            self.save()
        elif won:
            self.result = "User: {} has won".format(user.get_full_name())
            self.status = GAME_WON
            delta = datetime.datetime.now() - self.started_timestamp.replace(tzinfo=None)
            self.seconds += delta.seconds
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
        if cell.get('is_reveal', False):
            raise Exception(_('This cell is already revealed'))
        if cell.get('is_marked', False):
            raise Exception(_('This cell is already marked'))
        if not self.is_your_turn(user):
            raise Exception(_('Is not your turn to play'))
        cell.update({
            "is_marked": True
        })
        if [x, y] not in self.marked_cells:
            self.marked_cells.append([x, y])
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
        if not self.is_your_turn(user):
            raise Exception(_('Is not your turn to play'))
        cell.update({
            "is_marked": False
        })
        if [x, y] in self.marked_cells:
            self.marked_cells.remove([x, y])
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
        if not self.is_your_turn(user):
            raise Exception(_('Is not your turn to play'))
        cell.update({
            "is_reveal": True
        })
        if self.cell_has_boom(x, y):  # This cell has a boom
            cell.update({
                "has_boom": True
            })
            self.set_cell(x, y, cell)
            self.finish(user, boom=True, x=x, y=y)
        else:
            cell.update({
                "has_boom": False
            })
            if [x, y] in self.revelead_cells:
                self.revelead_cells.append([x, y])
            self.set_cell(x, y, cell)
            if cell.get('count', 0) == 0:  # This cell does not have adjacents
                self.__reveal_adjacents(user, cell.get('adjacents', []))

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

    @property
    def cells_simple_matrix(self):
        """
        Returns a matrix with string representation of the state of a cell
        * : Means the cell is not reveal
        (White Space): Means the cell is reveal
        F: Means the cell has been marked
        B: Means the cell has been revealed and has a boom
        [0-8]: Means the counter of adjancents cells with boom
        """
        matrix = [['*' for _ in range(0, self.columns)] for _ in range(0, self.rows)]

        for y, column in enumerate(matrix):
            for x, value in enumerate(column):
                cell = self.cell(x, y)
                if cell.get('is_reveal', False):  # The cell is reveal
                    if cell.get('has_boom', False):  # The cell has a boom
                        value = 'B'
                    elif cell.get('count', 0) == 0:  # The cell does not has adjacents
                        value = ' '
                    else:  # The cell does has adjacents
                        value = '{}'.format(cell.get('count', 0))
                else:
                    if cell.get('is_marked', False):  # The cell has been marked
                        value = 'F'
                matrix[y][x] = value
        return matrix

    @property
    def time_elapsed(self):
        sec = datetime.timedelta(seconds=self.get_seconds)
        d = datetime.datetime(1, 1, 1) + sec
        return _("Day (%d) Hours (%d) Minutes (%d) Seconds (%d)") % (d.day-1, d.hour, d.minute, d.second)

    @property
    def print_matrix(self):
        """
        Prints to console a matrix of string representation of the current state of the board
        """
        state = _("Started") if self.status == GAME_STARTED else _("Paused") if self.status == GAME_PAUSED \
            else _("FINISHED") if self.status in [GAME_WON, GAME_LOST] else _("UNDEFINED")
        print("State: {}".format(state))
        print("Rows: {} - Columns: {} - Booms: {}".format(self.rows, self.columns, self.mines_count))
        print("Time Elapsed: {}".format(self.time_elapsed))
        print(np.matrix(self.cells_simple_matrix))

    def pause(self, user):
        """
        Pause the time of the game to stop the timer and to prevent any user to do something on the game
        """
        if self.status not in [GAME_STARTED]:
            raise Exception(_('The game is not started'))
        if not self.is_your_turn(user):
            raise Exception(_('Is not your turn to play'))
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
        if not self.is_your_turn(user):
            raise Exception(_('Is not your turn to play'))
        self.status = GAME_STARTED
        self.started_timestamp = datetime.datetime.now()
        self.save()

    def restart(self, user):
        """
        Restart the board to start all over
        """
        if not self.is_your_turn(user):
            raise Exception(_('Is not your turn to play'))
        self.marked_cells = []
        self.revelead_cells = []
        for x in range(0, self.columns):
            for y in range(0, self.rows):
                cell = self.cell(x, y)
                cell.update({
                    "is_marked": False,
                    "is_reveal": False,
                    "has_boom": None,
                })
                self.set_cell(x, y, cell)
        self.seconds = 0
        self.started_timestamp = datetime.datetime.now()
        self.status = GAME_STARTED
        self.result = ""
        self.save()

