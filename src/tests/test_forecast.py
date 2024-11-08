import unittest
from datetime import datetime, date
from mongoengine import connect, disconnect
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)
from ormWP.models.woreda import Woreda
from ormWP.models.forecast import Forecast


class TestForecast(unittest.TestCase):
    def setUp(self):
        disconnect()
        connect('test_forecasts', host='mongomock://localhost')

        # Create a sample Woreda
        self.woreda = Woreda(
            name="Test Woreda",
            ext_id="TEST001"
        )
        self.woreda.save()

        # Create a sample Forecast
        self.forecast = Forecast(
            woreda=self.woreda,
            mean=3.123,
            date=date(2024, 11, 8)
        )

    def tearDown(self):
        disconnect()

    def test_create_forecast(self):
        self.forecast.save()

        # Assert that the Forecast has been saved and has an ID
        self.assertIsNotNone(self.forecast.id)

        # Fetch the Forecast from the database
        fetched_forecast = Forecast.objects(id=self.forecast.id).first()

        # Assert that the fetched Forecast matches the saved Forecast
        self.assertEqual(fetched_forecast.mean, 3.123)
        self.assertEqual(fetched_forecast.date, date(2024, 11, 8))
        self.assertEqual(fetched_forecast.trace['created_at'], fetched_forecast.trace['updated_at'])

    def test_update_forecast(self):
        self.forecast.save()
        

        # Update the Forecast's mean value
        self.forecast.mean = 2.456
        self.forecast.save()

        # Fetch the updated Forecast from the database
        updated_forecast = Forecast.objects(id=self.forecast.id).first()
        

        # Assert that the Forecast's mean has been updated
        self.assertEqual(updated_forecast.mean, 2.456)

    def test_delete_forecast(self):
        self.forecast.save()

        # Delete the Forecast
        self.forecast.delete()

        # Assert that the Forecast no longer exists in the database
        deleted_forecast = Forecast.objects(id=self.forecast.id).first()
        self.assertIsNone(deleted_forecast)

    def test_unique_forecast_per_woreda_and_date(self):
        self.forecast.save()

        # Attempt to create another Forecast with the same woreda and date
        duplicate_forecast = Forecast(
            woreda=self.woreda,
            mean=1.789,
            date=date(2024, 11, 8)
        )

        with self.assertRaises(Exception):
            duplicate_forecast.save()


if __name__ == "__main__":
    unittest.main()
