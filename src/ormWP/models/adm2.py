from mongoengine import Document, StringField, ReferenceField, ListField,DictField
from .adm1 import Adm1
class Adm2(Document):

    """
    Represents the adm2 levels in the database.

    Attributes:
    ----------
    name: str
        The name of the adm2.
    ext_id: str
        external id to identify.
    adm1: referencefield
        id of the adm1
    trace: array
        array with created time, updated and a active 

    Methods:
    -------
    save()
        Saves the Adm2 object to the database.
    delete()
        Deletes the Adm2 object from the database.
    """
    
    meta = {
        'collection': 'adm2'
    }
    name = StringField(max_length=150,required=True)
    ext_id = StringField(max_length=150, required=True)
    adm1 = ReferenceField(Adm1,required=True)
    trace = DictField()