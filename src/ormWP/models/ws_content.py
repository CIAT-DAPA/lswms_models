from mongoengine import Document, StringField, ReferenceField, ListField ,FloatField,DictField
from .watershed import Watershed
from .type_content import Typecontent
class Wscontent(Document):

    """
    Represents a watershed content in the database.

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
        Saves the watershedcontent object to the database.
    delete()
        Deletes the watershedcontent object from the database.
    """

    meta = {
        'collection': 'wscontent'
    }
    content=DictField()
    watershed=ReferenceField(Watershed)
    type= ReferenceField(Typecontent)