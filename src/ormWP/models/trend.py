from mongoengine import Document, ReferenceField, FloatField, DateField, DictField
from datetime import datetime, timezone
from .woreda import Woreda

class Trend(Document):
    """
    Represents a Trend in the database.

    Attributes:
    ----------
    woreda: ReferenceField
        Reference to the associated Woreda. Required.
    mean: float
        Mean value for the trend. Required.
    date: date
        Date for the trend. Required and unique per woreda.
    trace: dict
        Contains metadata such as created time, updated time.

    Methods:
    -------
    save()
        Saves the Trend object to the database, updating the 'updated_at' field in trace.
    delete()
        Deletes the Trend object from the database.
    """

    meta = {
        'collection': 'trends',
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
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc)
    })

    def save(self, *args, **kwargs):
        """Override save to update the 'updated_at' field."""
        now = datetime.now(timezone.utc)

        if not self.trace:
            self.trace = {
                'created_at': now,
                'updated_at': now
            }
        else:
            self.trace['updated_at'] = now

        
        self._mark_as_changed('trace')

        return super().save(*args, **kwargs)
        
