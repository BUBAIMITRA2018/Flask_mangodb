from flask import Flask
from flask import Flask, jsonify, request
from flask import Flask, request, Response
from flask_bcrypt import Bcrypt
from flask.json import dumps
from flask_bcrypt import Bcrypt
from database.db import initialize_db
from database.models import Chemical
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from numpy.f2py.crackfortran import debug, true_intent_list
from database.models import User
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
import datetime

app = Flask(__name__)

chemicals = [
{
"id": "1",
"ID": 6,
"Name": "C"
},
{
"id": "2",
"ID": 7,
"Name": "N"
},
{
"id": "3",
"ID": 8,
"Name": "O"
},
{
"id": "4",
"ID": 13,
"Name": "Al"
}
]

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/chemical'
}

app.config.from_envvar('ENV_FILE_LOCATION')



db = initialize_db(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

class ChemicalSchema(ma.Schema):  
        
    class Meta:
        # Fields to expose
        fields = ("ID", "Name")

chemical_schema = ChemicalSchema()
chemicals_schema = ChemicalSchema(many=True)


@app.route('/')
def hello():
    return   jsonify(chemicals)

@app.route('/chemicals', methods=['GET'])
# @jwt_required
def get_chemicals():
    chemicals = Chemical.objects().all()   
    return Response(chemicals_schema.dumps(chemicals))

@app.route('/createuser', methods=['POST'])
def createuser():
    body = request.get_json(force=True)
    user = User(**body)
    user.hash_password()
    user.save()
    id = user.id 
    return {'id': str(id)}, 200


@app.route('/login', methods=['POST'])
def login():
    body = request.get_json(force=True)
    user = User.objects.get(email=body.get('email'))
    authorized = user.check_password(body.get('password'))
    if not authorized:
        return {'error': 'Email or password invalid'}, 401
    expires = datetime.timedelta(days=7)
    access_token = create_access_token(identity=str(user.id), expires_delta=expires)
    return {'token': access_token}, 200
        

  



app.run(debug = True)