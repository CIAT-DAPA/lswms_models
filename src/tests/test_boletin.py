import unittest
from mongoengine import connect, disconnect
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)
from ormWP.models.suscription import Suscription, Boletin
from datetime import datetime

# Conectarse a la base de datos de prueba


class TestBoletin(unittest.TestCase):

    def setUp(self):
        disconnect()
        connect('test_water_points', host='mongomock://localhost')
        self.suscription = Suscription(
            userId='sjcne92929',
            boletin=Boletin.ALERT,
            waterpoint=['1828291jsjsj'],
            trace={"created": datetime.now(), "updated": datetime.now(), "enabled": True}
        )

    def test_create_suscription(self):
        self.suscription.save()
        self.assertIsNotNone(self.suscription.id)

        print(self.suscription)

        suscription = Suscription.objects(id=self.suscription.id).first()
        self.assertEqual(suscription.userId, 'sjcne92929')
        self.assertEqual(suscription.boletin, Boletin.ALERT)
        self.assertEqual(suscription.waterpoint, ['1828291jsjsj'])

if __name__ == '__main__':
    unittest.main()
