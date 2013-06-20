#!/usr/bin/env python2

import os
from gevent import monkey; monkey.patch_all()
from socketio import socketio_manage
from socketio.server import SocketIOServer
from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin
import mimetypes

class GitNamespace(BaseNamespace, BroadcastMixin):
    def on_proxy(self, ident, event):
        self.broadcast_event(ident, event)

    def recv_disconnect(self):
        self.disconnect(silent=True)

class Application(object):
    def __init__(self):
        self.request = {}
        self.index_page = "index.html"

    def __call__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

        if self.is_static:
            return self.get_static_file(self.path)

        if self.path.startswith("socket.io"):
            socketio_manage(environ, {"": GitNamespace}, self.request)
        else:
            return not_found(start_response)

    @property
    def path(self):
        "Returns the `PATH_INFO` from the WSGI environment or `self.index_page`."
        path = self.environ.get("PATH_INFO", "")

        if not path or path == "/":
            return self.index_page

        return path.strip("/")

    @property
    def is_static(self):
        "Returns True if the HTTP request is for a static file (js, css, html etc.)."
        return self.path.startswith("static/") or self.path == self.index_page

    def get_file_path(self, path=None):
        "Return the web server's root directory + the path."
        path = path if path else self.path
        file_directory = os.path.dirname(__file__)
        return os.path.join(file_directory, path)

    def guess_mimetype(self, path=None):
        "Returns the MIME type of a file in the form of a text string given the file path."
        return mimetypes.guess_type(self.get_file_path(path))[0]

    def get_static_file(self, path):
        "Returns the contents of a static file and begins the HTTP response."
        try:
            data = open(self.get_file_path(path)).read()
        except IOError:
            return not_found(self.start_response)

        self.start_response("200 OK", [
            ( "Content-Type", self.guess_mimetype(path) ),
        ], )

        return [data]

def not_found(start_response):
    start_response("404 Not Found", [])
    return ["<h1>Not Found</h1>"]

def emit_event(event_type, ident):
    "Fires off an event to the websocket endpoint, imported in the Git hook scripts."
    from socketIO_client import SocketIO

    with SocketIO("0.0.0.0", 80) as socketIO:
        socketIO.emit("proxy", ident, event_type)

def main():
    print "Server running"
    SocketIOServer(("0.0.0.0", 80), Application(),
        resource="socket.io", policy_server=True,
        policy_listener=("0.0.0.0", 10843)).serve_forever()

if __name__ == "__main__":
    main()