from mongoengine import Document, StringField, ReferenceField, ListField ,FloatField,DictField
from .watershed import Watershed

class Typecontent(Document):

    """
    Represents the type of content.

    Attributes:
    ----------
    name: string
        name of the content.
        
    Methods:
    -------
    save()
        Saves the Type object to the database.
    delete()
        Deletes the Type object from the database.
    """

    meta = {
        'collection': 'typcontent'
    }
    name=StringField(max_length=100,required=True)
    trace= DictField()