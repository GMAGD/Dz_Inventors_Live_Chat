
from flask import Flask, send_from_directory, redirect, url_for, request
from flask_socketio import SocketIO, rooms
import os
from chat import configure_chat

app = Flask(__name__)

app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
app.config['CACHE_TYPE'] = 'simple'  # You can use other cache types
socketio = SocketIO(app, cors_allowed_origins="*")


# flask routes here and socketio don't mix with other thing
# create seperate files

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    # Initialize and configure the chat module
    configure_chat(socketio)

    # Run the Flask app
    socketio.run(app, debug=True, host='0.0.0.0', port=8080)
