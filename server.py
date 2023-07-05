from flask import Flask

server = Flask(__name__)

@server.route('/')
def home():
    return '<p>Worked!</p>'

if __name__ == '__main__':
    server.run()
