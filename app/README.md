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