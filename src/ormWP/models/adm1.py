from mongoengine import Document, StringField, ReferenceField, FloatField, DictField, ListField


class Adm1(Document):

    """"
    Represents the adm1 in the database.

    Attributes:
    ----------
    name: str
        Name of the adm1. required.
    ext_id: str
        External identifier for the Adm1. Mandatory and unique.
    traced: array
        array with created time, updated and a active 
        
    Methods:
    -------
    save()
        Saves the Adm1 object to the database.
    delete()
        Deletes the Adm1 object from the database.
    """

    meta = {
        'collection': 'adm1'
    }
    name = StringField(max_length=150,required=True)
    ext_id = StringField(max_length=150, required=True)
    traced = ListField(required=True)