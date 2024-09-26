from flask import Flask, render_template, redirect
from flask_socketio import SocketIO, emit, join_room
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
sio = SocketIO(app)

if __name__ == '__main__':
    sio.run(app, debug=True)
