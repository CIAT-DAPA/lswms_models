from mongoengine import Document, DateTimeField, StringField, DictField, EnumField, ListField, ReferenceField
from enum import Enum

class Boletin(Enum):
    """"
    Represents the Boletin
    """
    ALERT = 'alert'
    WEEKLY = 'weekly'




class Suscription(Document):
    """"
    Represents a suscription in the database.

    Attributes:
    ----------
    userId: str
        Id of the user suscribed.
    boletin: str
        type of boletin.
    waterpoint: str
        id of the waterpoint
    trace: dict
        manage the trace of the suscription

    Methids:
    -------
    save()
        save the object in the database.
    delete()
        delete the object of the database.
    """
    meta = { 'collection': 'suscription'}

    userId = StringField(max_length=150, required=True)
    boletin = EnumField(Boletin, required=True)
    waterpoint = ListField()
    trace = DictField()