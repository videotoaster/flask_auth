from flask_auth import app
from sys import argv



if __name__ == "__main__":
    try:
        app.run("localhost", int(argv[1]))
    except:
        app.run("localhost")