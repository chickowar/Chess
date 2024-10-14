# Version 0.1.6

to run it you have to (in Chess\app):

```commandline
poetry install
poetry shell
poetry run python app\app.py
```

To access sqlite database (in pycharm community edition)
```jdbc:sqlite:{path to app}\Chess\app\instance\chess.db```

Note that (at least on windows) you have to download fonts,
restart your pc and only then the fonts will appear on the page properly

### This version will be done 'kinda' as a monolith

##### (meaning website logic will be in app\app.py and chess logic in app\chess_logic.py)

---
Commit - "Tracking and reverting moves"
1 room, working chess, no mate, no in-check state, tracks and reverts moves

### Changes:

1) Fixed a bug in MoveMaker.make_move which couldn't track whether rook is moved or not
   (it tried to remove white_r_left instead of white_rook_left from the set)
2) Fixed a major issue in MoveMaker.make_move: when king moves, it always tries to remove 'white_king' from the set,
   that throws error, if 'white_king' is already removed from the set.
3) Added MoveMaker.revert_last_move and changed the MoveMaker.make_move_safe functionality accordingly.
4) Added MoveMaker.prev_moves list attribute.
5) Changed the way MoveMaker is initialized (now it takes kings and unmoved_pieces as input)
6) Changed the way PieceChecker is initialized, so that now it is created from pos and
   the MoveMaker object, rather than from pos, board, turn
   (now it actually properly tracks king position and unmoved_pieces)
7) ***ADDED '-' AS A POSSIBLE INPUT ON THE WEBSITE*** which reverts the move!
8) Defined a notation in which moves will be stored in db and MoveMaker object.
9) Changed MoveMaker.pieces to fit 'str_str' style rather than 'StrStr' style.

#### Faults: no en passant, no mates, no proper in-check trigger

---
check todos in chess_logic.py

1) Next: en passant
2) after that: storing everything in sqlite
3) after that: proper room joining
4) after that: ...

I'll think later, but we have to make

1) Separate rooms, where you can log on (simple name and password for now), choose side and play with a friend.
2) Make a possibility of being a spectator for a game.
3) Make invite links
4) MAKE ACTUAL PROPER PLAYING BOARD WITH MOVING PIECE SVGs
5) Make a clock
6) Make a home page
7) REWRITE CODE TO STORE OBJECTS RATHER THAN TEXT (?)
8) Make actual sweden chess