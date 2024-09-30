var socket = io();
var roomId = document.getElementById('room-id').value;
var SubmitButton = document.getElementById('submit-move-button');
var MoveField = document.getElementById('move-field');

MoveField.addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        SubmitButton.click();
    }
});

console.log(roomId);

socket.emit('join', {room_id: roomId});
console.log('should have joined');

socket.on('update_board', function(board) {
    document.getElementById('board').innerHTML = board;
});

function submitMove() {
    MOVE = MoveField.value;
    MoveField.value = '';
    socket.emit('submit-move', {room_id: roomId, move: MOVE});
}
