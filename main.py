import sys
from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
# app = Flask(__name__)
app = Flask(__name__, static_url_path='', static_folder='./app/dist/app')
app.config['JSON_AS_ASCII'] = False


# @app.route('/')
# def hello():
#     """Return a friendly HTTP greeting."""
#     return 'Hello World!'

@app.route('/')
def angular():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
