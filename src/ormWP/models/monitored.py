from mongoengine import Document, StringField, ReferenceField, ListField ,FloatField, DateTimeField
from .waterpoint import Waterpoint

class Monitored(Document):

    """
    Represents a monitored data in the database.

    Attributes:
    ----------
    date: DateTime
        date from the historical data.
    values: array
        values of the monitored values.
    waterpoint: Waterpoint
        reference to waterpoint.

    Methods:
    -------
    save()
        Saves the monitored object to the database.
    delete()
        Deletes the monitored object from the database.
    """

    meta = {
        'collection': 'monitored'
    }
    date=DateTimeField(required=True)
    values=ListField(max_length=150,required=True)
    waterpoint=ReferenceField(Waterpoint)