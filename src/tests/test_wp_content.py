import unittest
from mongoengine import connect, disconnect
import sys
import os
from datetime import datetime
# Asegúrate de tener las rutas correctas para importar los módulos
dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)

from ormWP.models.waterpoint import Waterpoint
from ormWP.models.watershed import Watershed
from ormWP.models.adm1 import Adm1
from ormWP.models.adm2 import Adm2
from ormWP.models.adm3 import Adm3
from ormWP.models.type_content import Typecontent
from ormWP.models.wp_content import Wpcontent



# Conectarse a la base de datos de prueba


class Testwpcontent(unittest.TestCase):

    def setUp(self):
        # Desconectarse de cualquier conexión existente
        disconnect()
        connect('test_water_points', host='mongomock://localhost')

        # Crea un objeto Watershed de prueba
        self.adm1 = Adm1(
            name='zona prueba',
            ext_id='1132',
            trace={"created": datetime.now(), "updated": datetime.now(), "enabled": True}
        )
        self.adm1.save()

        # Crea un objeto Adm2 de prueba con referencia a Adm1
        self.adm2 = Adm2(
            name='subzona prueba',
            ext_id='456',
            trace={"created": datetime.now(), "updated": datetime.now(), "enabled": True},
            adm1=self.adm1
        )
        self.adm2.save()

        self.adm3 = Adm3(
            name='subsubzona prueba',
            ext_id='789',
            trace={"created": datetime.now(), "updated": datetime.now(), "enabled": True},
            adm2=self.adm2,
            aclimate_id='64ad5835515640e690d80dba'
        )
        self.adm3.save()

        # Crea un objeto Watershed de prueba con referencia a Adm2
        self.watershed = Watershed(
            area=100.0,
            name='watershed prueba',
            trace={"created": datetime.now(), "updated": datetime.now(), "enabled": True},
            adm3=self.adm3
        )
        self.watershed.save()
        # Crea un objeto Waterpoint de prueba con referencia a Watershed
        self.waterpoint = Waterpoint(
            lat=1.2345,
            lon=2.3456,
            name='waterpoint prueba',
            area=100.0,
            climatology=['climate1', 'climate2'],
            other_attributes=['attr1', 'attr2'],
            watershed=self.watershed,
            ext_id='512',
            trace={"created": datetime.now(), "updated": datetime.now(), "enabled": True}
        )

        self.waterpoint.save()

        # Crea un objeto Typecontent de prueba
        self.typecontent = Typecontent(
            name='typecontent prueba'
        )
        self.typecontent.save()

        self.wp_content = Wpcontent(
            content=[{'contenido1':'vacas','contenido2':'peronas'}],
            waterpoint=self.waterpoint,
            type=self.typecontent
        )
        # Crea un objeto Content de prueba con referencia a Waterpoint y Typecontent
        

    def tearDown(self):
        # Limpia la base de datos eliminando los objetos creados durante las pruebas
        self.waterpoint.delete()
        self.watershed.delete()
        self.adm3.delete()
        self.adm2.delete()
        self.adm1.delete()
        self.typecontent.delete()

    def test_create_content(self):
    # Guarda el objeto Content
        self.wp_content.save()
        self.assertIsNotNone(self.wp_content.id)

        # Verifica que el Content haya sido creado exitosamente
        self.assertEqual(self.wp_content.content, [{'contenido1':'vacas','contenido2':'peronas'}])
        self.assertEqual(self.wp_content.waterpoint, self.waterpoint)
        self.assertEqual(self.wp_content.type, self.typecontent)


        

if __name__ == '__main__':
    unittest.main()
