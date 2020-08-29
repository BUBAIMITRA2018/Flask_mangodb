from flask import Flask
from flask import Flask, jsonify, request
from flask import Flask, request, Response
from flask.json import dumps
from database.db import initialize_db
from database.models import Chemical
from flask_marshmallow import Marshmallow
from numpy.f2py.crackfortran import debug, true_intent_list

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

class ChemicalSchema(ma.Schema):  
        
    class Meta:
        # Fields to expose
        fields = ("ID", "Name")


user_schema = ChemicalSchema()
users_schema = ChemicalSchema(many=True)

@app.route('/')
def hello():
    return   jsonify(chemicals)

@app.route('/chemicals', methods=['GET'])
def get_chemicals():
    chemicals = Chemical.objects().all()   
    return Response(users_schema.dumps(chemicals))

app.run(debug = True)