from mongoengine import Document, StringField, ReferenceField,DictField
from .adm2 import Adm2
class Adm3(Document):

    """
    Represents the adm3 levels in the database.

    Attributes:
    ----------
    name: str
        name of the adm3.
    ext_id: str
        External id.
    adm2: referenciefield
        reference to an adm2.
    trace: array
       array with created time, updated and a active 
        
    Methods:
    -------
    save()
        Saves the Adm3 object to the database.
    delete()
        Deletes the Adm3 object from the database.
    """

    meta = {
        'collection': 'adm3'
    }
    name = StringField(max_length=100,required=True)
    ext_id = StringField(max_length=150, required=True)
    adm2 = ReferenceField(Adm2,required=True)
    trace= DictField()