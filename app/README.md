# Version 0.1.0
to run it you have to (in Chess\app):
```commandline
poetry install
poetry shell
poetry run python app\app.py
```

To access sqlite database (in pycharm)
```jdbc:sqlite:{path to app}\Chess\app\instance\chess.db```

### This version will be done 'kinda' as a monolith (meaning all the logic will be in app\app.py)
Commit - "Actual chess logic in piece movement"
1 room, working board, ACTUAL CHESS LOGIC, you take turns (you cant move white piece twice)
#### Faults: no castling, no en passant, no checks and mates
check todos in chess_logic.py

1) Next: Cosmetic changes to the board (i want to see numbers and letters)
2) after that: proper room joining
3) after that: storing everything in sqlite
4) after that: ... 

I'll think later, but we have to make

1) Separate rooms, where you can log on (simple name and password for now), choose side and play with a friend.
2) Make a possibility of being a spectator for a game.
3) Make invite links
4) MAKE ACTUAL PROPER PLAYING BOARD WITH MOVING PIECE SVGs
5) Make a clock
6) Make a home page
7) Make actual sweden chess