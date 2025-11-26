from mongoengine import Document, IntField, StringField, ReferenceField, EmbeddedDocumentField, DateTimeField
from .waterpoint import Waterpoint
from .probability import Probability


class SeasonalForecast(Document):
    """
    Represents a seasonal forecast in the database.

    Attributes:
    ----------
    year: int
        Year of the forecast.
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
        'collection': 'seasonal_forecast'
    }

    year = IntField(required=True)
    month = IntField(required=True, min_value=1, max_value=12)
    probabilities = EmbeddedDocumentField(Probability, required=True)
    waterpoint = ReferenceField(Waterpoint)

    created_at = DateTimeField()
    updated_at = DateTimeField()
    created_by = StringField()