# probability.py

from mongoengine import EmbeddedDocument, StringField, FloatField


class Probability(EmbeddedDocument):
    """
    Generic probability class used in both Seasonal and Subseasonal forecasts.
    """
    measure = StringField(required=True)
    below = FloatField(required=True)
    normal = FloatField(required=True)
    above = FloatField(required=True)