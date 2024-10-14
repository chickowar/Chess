# Version 0.1.5
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
Commit - "Fixed Castling"
1 room, working board, ACTUAL CHESS LOGIC, turn-based
### Changes:
1) Fixed Castling bug (it checked whether rook moved instead of whether it didn't in rook_unmoved. 
Which made castling impossible)

#### Faults: no en passant, no mates
check todos in chess_logic.py

1) Next: store moves for en passant
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
7) Make actual sweden chess