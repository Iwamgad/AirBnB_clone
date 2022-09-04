#!/usr/bin/python3
<<<<<<< HEAD

"""This module tests the BaseModel class"""

import unittest
from unittest import mock
from models.base_model import BaseModel
import models
from datetime import datetime


class TestBaseModel_Instantiation(unittest.TestCase):
    """A test class for the BaseModel class"""

    def no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)

    def test_args_unused(self):
        pass

    def test_instantiation_with_kwargs(self):
        dateTime = datetime.today()
        dt_iso = dateTime.isoformat()
        baseModel = BaseModel(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(baseModel.id, "123")
        self.assertEqual(baseModel.created_at, dateTime)
        self.assertEqual(baseModel.updated_at, dateTime)

    def test_instantiation_with_args_and_kwargs(self):
        dateTime = datetime.today()
        dt_iso = dateTime.isoformat()
        baseModel = BaseModel("12", id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(baseModel.id, "123")
        self.assertEqual(baseModel.created_at, dateTime)
        self.assertEqual(baseModel.updated_at, dateTime)


class TestBaseModel_to_dict(unittest.TestCase):
    """A test class for testing dict of the BaseModel class"""

    def test_to_dict(self):
        """Converts object attributes to dictionary for json"""

        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.my_number = 89
        d = my_model.to_dict()
        attributes = ["id", "created_at", "updated_at", "name", "my_number", "__class__"]
        self.assertCountEqual(d.keys(), attributes)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "ALX")
        self.assertEqual(d['my_number'], 89)

    def test_to_dict_type(self):
        baseModel = BaseModel()
        self.assertTrue(dict, type(baseModel.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        baseModel = BaseModel()
        self.assertIn("id", baseModel.to_dict())
        self.assertIn("created_at", baseModel.to_dict())
        self.assertIn("updated_at", baseModel.to_dict())
        self.assertIn("__class__", baseModel.to_dict())

    def test_to_dict_contains_added_attribute(self):
        baseModel = BaseModel()
        baseModel.name = "ALX"
        baseModel.my_number = 98
        self.assertIn("name", baseModel.to_dict())
        self.assertIn("my_number", baseModel.to_dict())

    def test_to_dict_datetime_attributes_str(self):
        baseModel = BaseModel()
        bm_dict = baseModel.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dateTime = datetime.today()
        baseModel = BaseModel()
        baseModel.id = "123876"
        baseModel.created_at = baseModel.updated_at = dateTime
        timeDict = {
            'id': '123876',
            '__class__': 'BaseModel',
            'created_at': dateTime.isoformat(),
            'updated_at': dateTime.isoformat()
        }
        self.assertDictEqual(baseModel.to_dict(), timeDict)

    def test_to_dict_with_arg(self):
        baseModel = BaseModel()
        with self.assertRaises(TypeError):
            baseModel.to_dict(None)


class TestBaseModel_save(unittest.TestCase):
    """A test class for testing save of the BaseModel class"""

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Tests the save method"""

        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)


if __name__ == "__main__":
    unittest.main()
=======
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
>>>>>>> 6228dc3a104c6838baf8ee6e89801d86ef875ae2
