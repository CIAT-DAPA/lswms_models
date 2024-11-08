from mongoengine import Document, ReferenceField, FloatField, DateField, DictField
from datetime import datetime
from .woreda import Woreda

class Forecast(Document):
    """
    Represents a Forecast in the database.

    Attributes:
    ----------
    woreda: ReferenceField
        Reference to the associated Woreda. Required.
    mean: float
        Mean value for the forecast. Required.
    date: date
        Date of the forecast. Required and unique per woreda.
    trace: dict
        Contains metadata such as created time and updated time.

    Methods:
    -------
    save()
        Saves the Forecast object to the database, updating the 'updated_at' field in trace.
    delete()
        Deletes the Forecast object from the database.
    """

    meta = {
        'collection': 'forecasts',
        'indexes': [
            {
                'fields': ['woreda', 'date'], 
                'unique': True
            }
        ]
    }

    woreda = ReferenceField(Woreda, required=True, reverse_delete_rule=2)
    mean = FloatField(required=True, precision=4)
    date = DateField(required=True)
    trace = DictField(default=lambda: {
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    })

    def save(self, *args, **kwargs):
        """Override save to update the 'updated_at' field."""
        if not self.trace:
            self.trace = {
                'created_at': datetime.now(),
                'updated_at': datetime.now()
            }
        else:
            self.trace['updated_at'] = datetime.now()

        
        self._mark_as_changed('trace')

        return super().save(*args, **kwargs)

