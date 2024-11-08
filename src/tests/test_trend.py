import unittest
from datetime import datetime, date, timezone
from mongoengine import connect, disconnect
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)
from ormWP.models.woreda import Woreda
from ormWP.models.trend import Trend


class TestTrend(unittest.TestCase):
    def setUp(self):
        disconnect()
        connect('test_trends', host='mongomock://localhost')
        
        # Create a sample Woreda
        self.woreda = Woreda(
            name="Test Woreda",
            ext_id="TEST001"
        )
        self.woreda.save()
        
        # Create a sample Trend
        self.trend = Trend(
            woreda=self.woreda,
            mean=3.234,
            date=date(2024, 11, 8)
        )

    def tearDown(self):
        disconnect()

    def test_create_trend(self):
        self.trend.save()

        # Assert that the Trend has been saved and has an ID
        self.assertIsNotNone(self.trend.id)

        # Fetch the Trend from the database
        fetched_trend = Trend.objects(id=self.trend.id).first()

        # Assert that the fetched Trend matches the saved Trend
        self.assertEqual(fetched_trend.mean, 3.234)
        self.assertEqual(fetched_trend.date, date(2024, 11, 8))
        self.assertEqual(fetched_trend.trace['created_at'], fetched_trend.trace['updated_at'])

    def test_update_trend(self):
        self.trend.save()

        # Update the Trend's mean value
        self.trend.mean = 2.123
        self.trend.save()

        # Fetch the updated Trend from the database
        updated_trend = Trend.objects(id=self.trend.id).first()

        # Assert that the Trend's mean has been updated
        self.assertEqual(updated_trend.mean, 2.123)


    def test_delete_trend(self):
        self.trend.save()

        # Delete the Trend
        self.trend.delete()

        # Assert that the Trend no longer exists in the database
        deleted_trend = Trend.objects(id=self.trend.id).first()
        self.assertIsNone(deleted_trend)

    def test_unique_trend_per_woreda_and_date(self):
        self.trend.save()

        # Attempt to create another Trend with the same woreda and date
        duplicate_trend = Trend(
            woreda=self.woreda,
            mean=4.456,
            date=date(2024, 11, 8)
        )

        with self.assertRaises(Exception):
            duplicate_trend.save()


if __name__ == "__main__":
    unittest.main()
