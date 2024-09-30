from flask import Flask, render_template, redirect, request, jsonify
from flask_socketio import SocketIO, emit, join_room
from flask_sqlalchemy import SQLAlchemy

from random import randint
from uuid import UUID, uuid4
import os

from chess_logic import MoveMaker

...


"Setting Up"
database_name = "chess.db"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'TotallySecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
sio = SocketIO(app)

# @TODO: Предположительно всё будет работать вызовом новых MoveMaker'ов от доски в бд,
# @TODO: потом они будут коммитить ход и уничтожаться... нврн так


...


"ORM"
def new_id():
    return int(randint(0,9223372036854775807))

class BoardTable(db.Model):
    id = db.Column(db.Integer, primary_key=True, default=new_id)
    board = db.Column(db.String(64), default='0'*64)

    def __repr__(self):
        return f"<board is {self.board}>"


...


"Socketio Handlers"
@sio.on('join')
def handle_join(data):
    room_id = data['room_id']
    join_room(room_id)  # пока что одна комната
    print(f'in-room {room_id}')
    emit('update_board', test_board.proper_board(), room=room_id)
    print('emitted')
    pass

@sio.on('submit-move')
def handle_submit_move(data):
    move = data['move']
    try:
        # print('handle_submit_move: trying to split')
        move_from, move_to = move.split('-')
        # print('handle_submit_move: trying_to_move')
        result = test_board.make_move_safe(move_from, move_to)
        print(result)
    except Exception as e:
        warn(f"IMPROPER MOVE - {move} | {e}")
    emit('update_board', test_board.proper_board(), room=data['room_id'],broadcast=True)
    pass


...


"Endpoints"
@app.route('/')
def home():
    return render_template('home.html')
    pass


# FOR TESTING
test_board = MoveMaker()


@app.route('/read/<the_id>')
def read_the_id(the_id):
    return str(read_board_table(the_id).board)

@app.route('/read/')
def read_all():
    l = {}
    a = BoardTable.query.all()
    for i in a:
        l[i.id] = i.board
    return jsonify(l)

@app.route('/create/', methods=['POST', 'GET'])
def create_board():
    if request.method == 'POST':
        # print(request.form)
        try:
            the_id = new_id()
            new_board = BoardTable(id=the_id, board=request.form['board'])
            append_db(db, new_board)
            return redirect(f'/read/{the_id}')
        except Exception as e:
            warn(f"EXCEPTION: {e} thrown in create_board")
    return render_template('create_form.html')


...


"Utils"
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def warn(text):
    print(bcolors.WARNING + text + bcolors.ENDC)

def append_db(database: SQLAlchemy, data: BoardTable, with_id: int | None = None):
    try:
        database.session.add(data)
        database.session.commit()
        warn('committed')
        if with_id:
            warn(f"{with_id} {read_board_table(with_id)}")
    except Exception as e:
        warn(f"{e} thrown in append_db({data})")

def read_board_table(pk: int):
    return BoardTable.query.get_or_404(pk)


"Launch"
if __name__ == '__main__':
    # launching from C:\progproj\CHESS\CHESS-1\Chess\app
    if not os.path.exists('./instance/' + database_name):
        print('creating db')
        with app.app_context():
            db.create_all()
    sio.run(app, debug=True)
