# AirBnB clone - The console
## Table of Content
1. [Project Description](#Project-Description)
2. [Environment Used](#Environment-Used)
3. [How to install it](#How-to-install-it)
4. [File Content](#File-Content)
5. [How to use it](#Usage)
6. [Examples of Use](#Examples-of-Use)
7. [Bugs](#Bugs)
8. [Authors](#Authors)
9. [License](#License)

## 1. Project Description
#### This project is the first part of the AirBnB project which is designed to teach us how to create objects, serialize files and create storage engine (The File Storage). A command interpreter is created in this project to manage AirBnB objects.
What this command interpreter does:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## 2. Environment Used
#### This project is interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
## 3. How to install it
1. Clone this repository: ```git clone "https://github.com/Iwamgad/AirBnB_clone.git" ```
2. Access the AirBnb directory: ```cd AirBnB_clone```
3. Run hbnb(interactively): ```./console and enter command```
4. Run hbnb(non-interactively): ```echo "<command>" | ./console.py```
## 4. File Content
[console.py](console.py) - This file contains the entry point of the command interpreter.

List of commands implemented on this console:
1. `quit` -  Exits the program.
2. `create` - Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
3. `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
4. `show` - Prints the string representation of an instance based on the class name and id.
5.  `all` - Prints all string representation of all instances based or not on the class name. 
6. `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

#### The first directory `models/` contains files with the main classes and one directory `engine/` . 
[base_model.py](/models/base_model.py) - This is the parent class.
* `def __init__(self, *args, **kwargs)` - Initializes a new BaseModel object.
* `def __str__(self)` - Returns the string representation of the BaseModel class.
* `def save(self)` - Updates the public instance attribute updated_at with the current datetime.
* `def to_dict(self)` - Returns a dictionary containing all keys/values of __dict__ of the instance.

Classes inherited from the BaseModel class:
1. [amenity.py](/models/amenity.py)
2. [city.py](/models/city.py)
3. [place.py](/models/place.py)
4. [review.py](/models/review.py)
5. [state.py](/models/state.py)
6. [user.py](/models/user.py)

#### The second directory `tests/` contains all the unit test cases used.
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the TestBaseModel and TestBaseModelDocs classes.

TestBaseModelDocs class:
* `def setUpClass(cls)`- Sets up for the doc tests
* `def test_bm_module_docstring(self)` - Tests for the base_model.py module docstring
* `def test_bm_class_docstring(self)` - Tests for the BaseModel class docstring
* `def test_bm_func_docstrings(self)` - Tests for the presence of docstrings in BaseModel methods

TestBaseModel class:
* `def test_is_base_model(self)` - Tests that the instatiation of a BaseModel works
* `def test_created_at_instantiation(self)` - Tests created_at is a pub. instance attribute of type datetime
* `def test_updated_at_instantiation(self)` - Tests updated_at is a pub. instance attribute of type datetime
* `def test_diff_datetime_objs(self)` - Tests That two BaseModel instances have different datetime objects

[/test_models/test_amenity.py](/tests/test_models/test_amenity.py) - Contains the TestAmenityDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_amenity_module_docstring(self)` - Tests for the amenity.py module docstring
* `def test_amenity_class_docstring(self)` - Tests for the Amenity class docstring

[/test_models/test_city.py](/tests/test_models/test_city.py) - Contains the TestCityDocs class:
* `def test_pep8_conformance_test_city(self)` - Tests that tests/test_models/test_city.py conforms to PEP8
* `def test_city_module_docstring(self)` - Tests for the city.py module docstring
* `def test_city_class_docstring(self)` - Tests for the City class docstring

[/test_models/test_file_storage.py](/tests/test_models/test_file_storage.py) - Contains the TestFileStorageDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_file_storage_module_docstring(self)` - Tests for the file_storage.py module docstring

[/test_models/test_place.py](/tests/test_models/test_place.py) - Contains the TestPlaceDoc class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_place_module_docstring(self)` - Tests for the place.py module docstring
* `def test_place_class_docstring(self)` - Tests for the Place class docstring

[/test_models/test_review.py](/tests/test_models/test_review.py) - Contains the TestReviewDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_review_module_docstring(self)` - Tests for the review.py module docstring
* `def test_review_class_docstring(self)` - Tests for the Review class docstring

[/test_models/state.py](/tests/test_models/test_state.py) - Contains the TestStateDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_state_module_docstring(self)` - Tests for the state.py module docstring
* `def test_state_class_docstring(self)` - Tests for the State class docstring

[/test_models/user.py](/tests/test_models/test_user.py) - Contains the TestUserDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_user_module_docstring(self)` - Tests for the user.py module docstring
* `def test_user_class_docstring(self)` - Tests for the User class docstring


## 5. Examples of use
root@6c09b9266a56:~/AirBnB_clone# ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
bdfbf13e-bb9b-4ba9-b0ac-cc7d2160c059
(hbnb) all BaseModel
["[BaseModel](dab859ff-d70c-4abb-bc35-4bd2dcfc51be) {'id': 'dab859ff-d70c-4abb-bc35-4bd2dcfc51be', 
'name': 'My First Model', 'updated_at': datetime.datetime(2022, 9, 4, 9, 45, 54, 962502), 'my_number': 89, 
'created_at': datetime.datetime(2022, 9, 4, 9, 45, 54, 961631)}", "[BaseModel](25ee6189-a750-4899-bdd5-f835a0af75e5) 
{'id': '25ee6189-a750-4899-bdd5-f835a0af75e5', 'updated_at': datetime.datetime(2022, 9, 4, 9, 46, 19, 366996), 'created_at': 
datetime.datetime(2022, 9, 4, 9, 46, 19, 366996)}", "[BaseModel](c2b2cef7-3ee3-44de-9ffd-711b6fbe5bf1) {'id': 'c2b2cef7-3ee3-44de-9ffd-711b6fbe5bf1', 
'name': 'My_First_Model', 'updated_at': datetime.datetime(2022, 9, 4, 12, 53, 19, 268032), 'my_number': 89, 'created_at': datetime.datetime(2022, 9, 4, 12, 53, 19, 268032)}",
 "[BaseModel](d68b357d-f87f-42ef-b74a-7e29d67e8e94) {'id': 'd68b357d-f87f-42ef-b74a-7e29d67e8e94', 'name': 'My_First_Model', 'updated_at': datetime.datetime(2022, 9, 4, 9, 49, 1, 263242), 
 'my_number': 89, 'created_at': datetime.datetime(2022, 9, 4, 9, 49, 1, 262941)}", "[BaseModel](0b9837ad-66ef-49b3-a1bb-8c8468c4b305) {'id': '0b9837ad-66ef-49b3-a1bb-8c8468c4b305', 'name': 'My_First_Model',
 'updated_at': datetime.datetime(2022, 9, 4, 9, 50, 17, 266645), 'my_number': 89, 'created_at': datetime.datetime(2022, 9, 4, 9, 50, 17, 266166)}", "[BaseModel](bdfbf13e-bb9b-4ba9-b0ac-cc7d2160c059) 
 {'id': 'bdfbf13e-bb9b-4ba9-b0ac-cc7d2160c059', 'updated_at': datetime.datetime(2022, 9, 4, 22, 41, 56, 178753), 'created_at': datetime.datetime(2022, 9, 4, 22, 41, 56, 178753)}", "[BaseModel](24011e9d-5143-48dc-bbec-ea4f0b5bb08e)
 {'id': '24011e9d-5143-48dc-bbec-ea4f0b5bb08e', 'name': 'My_First_Model', 'updated_at': datetime.datetime(2022, 9, 4, 12, 52, 53, 164742), 'my_number': 89, 'created_at': datetime.datetime(2022, 9, 4, 12, 52, 53, 164232)}", 
 "[BaseModel](474c46a9-375e-420c-b9f5-513d302e9a5d) {'id': '474c46a9-375e-420c-b9f5-513d302e9a5d', 'name': 'My_First_Model', 'updated_at': datetime.datetime(2022, 9, 4, 9, 49, 55, 559930), 'my_number': 89, 'created_at': datetime.datetime(2022, 9, 4, 9, 49, 55, 559546)}", 
 "[BaseModel](db91c150-633c-4116-b20b-c886bcae2b71) {'id': 'db91c150-633c-4116-b20b-c886bcae2b71', 'name': 'My_First_Model', 'updated_at': datetime.datetime(2022, 9, 4, 12, 52, 53, 67676), 'my_number': 89, 'created_at': datetime.datetime(2022, 9, 4, 12, 52, 53, 67676)}", 
 "[BaseModel](3340eeda-77c6-4480-b233-d83198a1719c) {'id': '3340eeda-77c6-4480-b233-d83198a1719c', 'updated_at': datetime.datetime(2022, 9, 4, 12, 59, 9, 763866), 'created_at': datetime.datetime(2022, 9, 4, 12, 59, 9, 763866)}", "[BaseModel](3f876379-be96-4860-b99b-5d41c6422a9d)
 {'id': '3f876379-be96-4860-b99b-5d41c6422a9d', 'name': 'My First Model', 'updated_at': datetime.datetime(2022, 9, 4, 12, 54, 1, 764796), 'my_number': 89, 'created_at': datetime.datetime(2022, 9, 4, 12, 54, 1, 764033)}", "[BaseModel](9bf1e89f-9ff9-4a32-a694-db1a9ee3e642) 
 {'id': '9bf1e89f-9ff9-4a32-a694-db1a9ee3e642', 'updated_at': datetime.datetime(2022, 9, 4, 14, 46, 36, 697072), 'created_at': datetime.datetime(2022, 9, 4, 14, 46, 36, 697072), 'first_name': 'Betty'}", "[BaseModel](9a21b8d0-9455-43e5-ad88-6f8dce04535a) {'id': '9a21b8d0-9455-43e5-ad88-6f8dce04535a',
 'name': 'My_First_Model', 'updated_at': datetime.datetime(2022, 9, 4, 12, 53, 19, 363713), 'my_number': 89, 'created_at': datetime.datetime(2022, 9, 4, 12, 53, 19, 362880)}"]

(hbnb) destroy BaseModel bdfbf13e-bb9b-4ba9-b0ac-cc7d2160c059
(hbnb) show BaseModel bdfbf13e-bb9b-4ba9-b0ac-cc7d2160c059
** no instance found **
(hbnb) quit
root@6c09b9266a56:~/AirBnB_clone#
Documented commands (type help <topic>):

## 6. Bugs
#### No known bugs at this time
## 7. Authors
|Name | Github Account|
|-----|-------|
|Dagmawi Andualem|[Github](https://github.com/Iwamgad)|
|Tsion Zerihun|[Github](https://github.com/TsionZerihun)|

## 8. License
Public Domain. No copy write protection.
