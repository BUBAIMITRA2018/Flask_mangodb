from app.app import app
from flask_marshmallow import Marshmallow
from .models import Chemical

ma = Marshmallow(app)
 
class ChemicalSchema(ma.Schema):  
        
    class Meta:
        # Fields to expose
        fields = ("ID", "Name")


user_schema = ChemicalSchema()
users_schema = ChemicalSchema(many=True)