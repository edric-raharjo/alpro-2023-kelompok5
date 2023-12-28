import os

from flask import Flask
from Main import app as application


if __name__ == "__main__":
    host = os.environ.get("FLASK_HOST", "127.0.0.1")
    port = os.environ.get("FLASK_PORT", "8001")
    application.run(host=host, port=port)