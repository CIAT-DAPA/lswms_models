from mongoengine import Document, StringField, ReferenceField, ListField ,FloatField,DictField
from .watershed import Watershed

class Waterpoint(Document):

    """
    Represents a waterpoint in the database.

    Attributes:
    ----------
    lat: float
        Latitude of the waterpoint.
    lon: float
        Longitude of the waterpoint.
    name: str
        name of the waterpoint.
    area: float
        area of the waterpoint
    climatology: array
        historical dada from of the waterpoint
    watershed: Watershed
        reference to watershed
    other_atributes: array
        other attributes for the waterpoint
        
    Methods:
    -------
    save()
        Saves the waterpoint object to the database.
    delete()
        Deletes the waterpoint object from the database.
    """

    meta = {
        'collection': 'waterpoint'
    }
    lat=FloatField(max_length=100,required=True)
    lon=FloatField(max_length=100,required=True)
    name=StringField(max_length=100,required=True)
    area=FloatField(max_length=100,required=True)
    ext_id=StringField(max_length=100,required=True)
    climatology=ListField(required=False)
    other_attributes=ListField(required=False)
    watershed=ReferenceField(Watershed)
    trace= DictField()