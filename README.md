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

# 6. Bugs
#### No known bugs at this time
# 7. Authors
|Name | Github Account|
|-----|-------|
|Dagmawi Andualem|[Github](https://github.com/Iwamgad)|
|Tsion Zerihun|[Github](https://github.com/TsionZerihun)|

# 8. License
Public Domain. No copy write protection.