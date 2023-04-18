from flask_server import create_app
from .flask_server import HOST_NAME, HOST_PORT
app = create_app()

if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)