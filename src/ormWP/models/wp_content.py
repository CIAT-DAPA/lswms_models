from mongoengine import Document, StringField, ReferenceField, ListField ,FloatField,DictField
from .waterpoint import Waterpoint
from .type_content import Typecontent

class Wpcontent(Document):

    """
    Represents a waterpoint content in the database.

    Attributes:
    ----------
    content: array
        array with the content.
    type: Typecontent
        reference of the typecontent id.
    watershed: Watershed
        reference of the Watershed id.
   
    Methods:
    -------
    save()
        Saves the waterpointcontent object to the database.
    delete()
        Deletes the waterpointcontent object from the database.
    """

    meta = {
        'collection': 'wpcontent'
    }
    content=DictField()
    waterpoint=ReferenceField(Waterpoint)
    type= ReferenceField(Typecontent)