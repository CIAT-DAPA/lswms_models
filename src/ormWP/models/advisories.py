from mongoengine import Document, StringField, DictField
from datetime import datetime, timezone

class Advisory(Document):
    """
    Represents an Advisory text in the database.

    Attributes:
    ----------
    state: str
        Advisory state (GOOD, WATCH, ALERT, SEASONAL_DRY, NEAR_DRY). Required and unique.
    languages: dict
        Dictionary of translations keyed by language code (e.g., "en", "am", "or"). Required.
    trace: dict
        Contains metadata such as created_at and updated_at timestamps.
    """

    meta = {
        'collection': 'advisory',
        'indexes': [
            {
                'fields': ['state'],
                'unique': True
            }
        ]
    }

    state = StringField(
        required=True,
        choices=["GOOD", "WATCH", "ALERT", "SEASONAL_DRY", "NEAR_DRY"],
        unique=True
    )
    languages = DictField(required=True)  # {"en": "...", "am": "...", "or": "..."}

    trace = DictField(default=lambda: {
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc)
    })
