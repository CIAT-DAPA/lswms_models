from mongoengine import Document, StringField, DictField
from datetime import datetime,timezone

class Woreda(Document):
    """
    Represents a Woreda in the database.

    Attributes:
    ----------
    name: str
        Name of the Woreda. Required.
    ext_id: str
        External identifier for the Woreda. Required and unique.
    trace: dict
        Contains metadata such as created time, updated time, and enabled status.
    
    Methods:
    -------
    save()
        Saves the Woreda object to the database, updating the 'updated_at' field in trace.
    delete()
        Deletes the Woreda object from the database.
    """

    meta = {
        'collection': 'woredas',
        'indexes': [
            {
                'fields': ['ext_id'], 
                'unique': True
            }
        ]
    }

    name = StringField(max_length=255, required=True)
    ext_id = StringField(max_length=255, required=True, unique=True)
    trace = DictField(default=lambda: {
        'created_at': datetime.now(),
        'updated_at': datetime.now(),
        'enabled': True
    })

    def save(self, *args, **kwargs):
        """Override save to update the 'updated_at' field."""
        now = datetime.now(timezone.utc)

        if not self.trace:
            # Initialize the trace field if it's missing
            self.trace = {
                'created_at': now,
                'updated_at': now,
                'enabled': True 
            }
        else:
            # Update the 'updated_at' field
            self.trace['updated_at'] = now

        # Explicitly mark the 'trace' field as modified
        self._mark_as_changed('trace')

        # Persist changes
        return super().save(*args, **kwargs)
        

