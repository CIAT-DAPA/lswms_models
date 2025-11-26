from mongoengine import Document, IntField, StringField, ReferenceField, EmbeddedDocumentField, DateTimeField
from .waterpoint import Waterpoint
from .probability import Probability


class SubseasonalForecast(Document):
    """
    Represents a subseasonal forecast in the database.

    Attributes:
    ----------
    year: int
        Year of the forecast.
    month: int
        Month of the forecast (1–12).
    week: int
        Week number within the month (1–4).
    probabilities: Probability
        Probability object containing measure, below, normal, and above values.
    waterpoint: Waterpoint
        Reference to the associated waterpoint.
    created_at: DateTime
        Datetime when the forecast was created.
    updated_at: DateTime
        Datetime when the forecast was last updated.
    created_by: str
        User or system that created this forecast.
    """

    meta = {
        'collection': 'subseasonal_forecast'
    }

    year = IntField(required=True)
    month = IntField(required=True, min_value=1, max_value=12)
    week = IntField(required=True, min_value=1, max_value=4)

    probabilities = EmbeddedDocumentField(Probability, required=True)
    waterpoint = ReferenceField(Waterpoint)

    created_at = DateTimeField()
    updated_at = DateTimeField()
    created_by = StringField()