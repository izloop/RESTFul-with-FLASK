#Peter Levi Hornig - RESTful using FLASK RESTful in Python
# This uses CRUD (CREATE, READ, UPDATE & DELETE) so that we can
# add new users, read their data, update and then also if need be delete it


from flask import Flask
from flask_restful import Api, Resource, reqparse

#using Python Flask for this API structure
app = Flask(__name__)
api = Api(app)

#User template - a dictionary - replaces a SQL database as a store -
#classification ranges from 1 - 4 - the official classification by BisFED
users = [
    {
        "name": "David",
        "classification": 2,
        "occupation": "Boccia Player UK"
    },
    {
        "name": "Petra",
        "classification": 4,
        "occupation": "Boccia Player GER"
    },
    {
        "name": "Paola",
        "classification": 1,
        "occupation": "Boccia Player ES"
    }
    {
        "name": "Santino",
        "classification": 3,
        "occupation": "Boccia Player BR"
    }
]

class User(Resource):

#gets user details by specifying the name
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

#post creates a new entry into the API method - it accepts their name, classification and boccia player country
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("classification")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "classification": args["classification"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

#put allows us to either update details of a user or create new details if the user
#has not yet been created
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("classification")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["classification"] = args["classification"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name": name,
            "classification": args["classification"],
            "occupation": args["occupation"]

        }
        users.append(user)
        return user, 201

#deleting a user from the table
    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

#specifying the route of the API
api.add_resource(User, "/user/<string:name>")

app.run(debug=True)
