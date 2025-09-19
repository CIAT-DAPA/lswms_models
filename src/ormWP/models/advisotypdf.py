from mongoengine import Document, StringField, EnumField
from enum import Enum


class AdvisoryTypeEnum(Enum):
    """Enum for advisory PDF type"""
    SEASONAL = "seasonal"
    SUBSEASONAL = "subseasonal"


class AdvisoryPdf(Document):
    """
    Represents the AdvisoryPdf in the database.

    Attributes
    ----------
    type : str
        Advisory type. Must be 'seasonal' or 'subseasonal'.
    filename : str
        Name of the PDF file.
    description : str
        Detailed description of the advisory PDF.

    Methods
    -------
    save()
        Saves the AdvisoryPdf object to the database.
    delete()
        Deletes the AdvisoryPdf object from the database.
    """

    meta = {
        'collection': 'advisorypdf'
    }

    type = EnumField(AdvisoryTypeEnum, required=True)
    filename = StringField(max_length=255, required=True)
    name = StringField(max_length=255, required=True)
    description = StringField()
