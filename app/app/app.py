from flask import Flask, render_template, redirect, request, jsonify
from flask_socketio import SocketIO, emit, join_room
from flask_sqlalchemy import SQLAlchemy

from random import randint
from uuid import UUID, uuid4
import os

"Setting Up"
database_name = "chess.db"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'TotallySecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
sio = SocketIO(app)


"ORM"
def new_id():
    return int(randint(0,9223372036854775807))

class BoardTable(db.Model):
    id = db.Column(db.Integer, primary_key=True, default=new_id)
    board = db.Column(db.String(64), default='0'*64)

    def __repr__(self):
        return f"<board is {self.board}>"


"Socketio Handlers"


"Endpoints"
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        pass
    return render_template('home.html')

# FOR TESTING
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
            newboard = BoardTable(id=the_id, board=request.form['board'])
            append_db(db, newboard)
            return redirect(f'/read/{the_id}')
        except Exception as e:
            print(f"{e} thrown in create_board")
    return render_template('create_form.html')


"Utils"
def append_db(database: SQLAlchemy, data: BoardTable, with_id: int | None = None):
    try:
        database.session.add(data)
        database.session.commit()
        print('committed')
        if with_id:
            print(with_id, read_board_table(with_id))
    except Exception as e:
        print(f"{e} thrown in append_db({data})")

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
