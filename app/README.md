# Version 0.1.4
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
Commit - "Added castle and banned king-endangerment"
1 room, working board, ACTUAL CHESS LOGIC, turn-based
### Changes:
1) Now MoveMaker doesn't create new board if board is passed on as a list,
which means PieceChecker doesn't create a new board when created from
MoveMaker object's board.
2) Added king_moved dict and kings dict to MoveMaker, tracking whether
a king has moved and where he is located (respectively).
3) Fixed a bug in which kings were able to eat their citizens
4) make_move now tracks if you move a king
5) added lambda functions is_king, is_pawn, etc. which return True 
if you pass lowercase letter of the fitting piece into the function
6) ADDED there_is_check FUNCTION TO PieceChecker! Now if you make PieceChecker 
object out of white piece you can check whether white king would be in danger on 
a certain tile. !!! WARNING !!! The there_is_check function only checks for checks on 
the board specifically and doesn't say whether the move by king there is actually possible
That makes stuff like that occur: [+ + Tk+] where the tile to the right of the king is 
not in check, even though moving king there is not possible.
7) make_move_safe now detects if after you move a piece, the king would be in danger and reverts the move if so.
8) Added actual castling logic.

#### Faults: no en passant, no mates
check todos in chess_logic.py

1) Next: en passant
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