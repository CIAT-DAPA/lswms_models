import unittest
from mongoengine import connect, disconnect
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)
from ormWP.models.woreda import Woreda

class TestWoreda(unittest.TestCase):
    def setUp(self):
        disconnect() 
        connect('test_water_points', host='mongomock://localhost') 
        self.woreda = Woreda(
            name="Test Woreda",
            ext_id="TEST001"
        )

    def tearDown(self):
        disconnect()

    def test_create_woreda(self):
        # Save the Woreda to the database
        self.woreda.save()

        # Assert that the Woreda has been saved and has an ID
        self.assertIsNotNone(self.woreda.id)

        # Fetch the Woreda from the database
        fetched_woreda = Woreda.objects(id=self.woreda.id).first()

        # Assert that the fetched Woreda matches the saved Woreda
        self.assertEqual(fetched_woreda.name, "Test Woreda")
        self.assertEqual(fetched_woreda.ext_id, "TEST001")
        self.assertTrue(fetched_woreda.trace['enabled'])

    def test_update_woreda(self):
        # Save the Woreda to the database
        self.woreda.save()

        # Update the Woreda's name
        self.woreda.name = "Updated Woreda"
        self.woreda.save()

        # Fetch the updated Woreda from the database
        updated_woreda = Woreda.objects(id=self.woreda.id).first()

        # Assert that the Woreda's name has been updated
        self.assertEqual(updated_woreda.name, "Updated Woreda")
        self.assertNotEqual(updated_woreda.trace['updated_at'], updated_woreda.trace['created_at'])

    def test_delete_woreda(self):
        # Save the Woreda to the database
        self.woreda.save()

        # Delete the Woreda
        self.woreda.delete()

        # Assert that the Woreda no longer exists in the database
        deleted_woreda = Woreda.objects(id=self.woreda.id).first()
        self.assertIsNone(deleted_woreda)

if __name__ == '__main__':
    unittest.main()
