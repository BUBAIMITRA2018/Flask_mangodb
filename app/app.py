from flask import Flask
from flask import Flask, jsonify, request
from flask import Flask, request, Response
from flask_bcrypt import Bcrypt
from flask.json import dumps
from flask_bcrypt import Bcrypt
from database.db import initialize_db
from database.models import Chemical
from flask_marshmallow import Marshmallow
from numpy.f2py.crackfortran import debug, true_intent_list
from database.models import User

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



db = initialize_db(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)

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
def get_chemicals():
    chemicals = Chemical.objects().all()   
    return Response(chemical_schema.dumps(chemicals))

@app.route('/createuser', methods=['POST'])
def createuser():
    body = request.get_json(force=True)
    user = User(**body)
    user.hash_password()
    user.save()
    id = user.id 
    return {'id': str(id)}, 200
  



app.run(debug = True)