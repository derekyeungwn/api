from flask_restful import Resource, reqparse

users = [
    {
        'name': 'derek',
    },
    {
        'name': 'mary',
    }
]

class User(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True, help='Email is required')
    parser.add_argument('password', required=True, help='Password is required')

    def get(self, name):
        return {
            'message': '123'
        }, 403

    def post(self, name):
        return {
            'message': 'Add done!',
        }

    def put(self, name):
        return {
            'message': 'Udpate done!',
        }

    def delete(self, name):
        return {
            'message': 'Delete done!',
        }

class Users(Resource):
    def get(self):
        return {
            'message': '',
            'users': users
        }