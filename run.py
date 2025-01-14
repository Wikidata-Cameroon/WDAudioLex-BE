import os
from flask import Flask
from flask_restful import Api, Resource, reqparse
import datetime
from flask_swagger_ui import get_swaggerui_blueprint
from app import create_app 

app = Flask(__name__)

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
API_URL,
config={  # Swagger UI config overrides
'app_name': "Test application"
},
# oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
#    'clientId': "your-client-id",
#    'clientSecret': "your-client-secret-if-required",
#    'realm': "your-realms",
#    'appName': "your-app-name",
#    'scopeSeparator': " ",
#    'additionalQueryStringParams': {'test': "hello"}
# }
)

app.register_blueprint(swaggerui_blueprint)

api = Api(app)

new_user_post_args = reqparse.RequestParser()
new_user_post_args.add_argument("name",
type=str,
help="You must input a name.",
required=True)

new_user_post_args.add_argument("age",
type=int,
help="You must specify the age for a given name.",
required=False)

class NewUser(Resource):
def post(self):
args = new_user_post_args.parse_args()
age = args['age']
name = args['name']
now = datetime.datetime.now()
response = {
'name': name,
'age': age,
'created_on': now.strftime("%m/%d/%Y, %H:%M:%S")
}
return response

api.add_resource(NewUser, "/api/new_user")

@app.route("/")
def hello_world():
return "<p>Hello, World!</p>"

# Print the current working directory to confirm the app is running from the right place
print(f"Current working directory: {os.getcwd()}")

# Create the Flask app
app = create_app()

# Run the app
if __name__ == '__main__':
app.run(debug=True)  # Run the app in debug mode