import sys
from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource

from server.const.const import User, Conversation, Host, Visit

from server.util.logger import Logger

from server.datastore.datastore_manager import DatastoreManager


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
# app = Flask(__name__)
app = Flask(__name__, static_url_path='', static_folder='./app/dist/app')
app.config['JSON_AS_ASCII'] = False
api = Api(app)

log = Logger("DatastoreManager")


class User(Resource):

    def get(self):
        json_data = request.get_json(force=True)
        username = json_data[User.KEY_USER_NAME]
        thumb_url = json_data[User.KEY_THUMB_URL]
        dataManager = DatastoreManager()
        dataManager.get_user(username)
        return jsonify(u=username)

    def post(self):
        log.debug('post')
        user = request.json
        log.debug('post')

        dataManager = DatastoreManager()
        return dataManager.create_user(user)

    def put(self, userString):
        return


# @app.route('/users/<int:userid>', methods=['GET'])
# def get_user(userid=None):
#     dataManager = DatastoreManager()
#     return dataManager.get_user(userid)
    # return app.send_static_file('index.html')


@app.route('/callback/<input>')
def callback(input):
    log.debug('callback')
    # dataManager = DatastoreManager()
    # dataManager.create_user(input)
    return app.send_static_file('index.html')


@app.route('/')
def angular():
    log.debug('Root')
    return app.send_static_file('index.html')


api.add_resource(User, '/users')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
