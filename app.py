from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret!'
socketio = SocketIO(app)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@socketio.on("connect")
def handle_connect():
    print("Client has connected!!!")
    
@socketio.on("disconnect")
def handle_disconnect():
    print("Client has disconnect")
    
@socketio.on("message")
def handle_message(message):
    print("Message recived")
    print(message)
    socketio.emit("message", message)

if __name__ == "__main__":
    socketio.run(app, debug=True)