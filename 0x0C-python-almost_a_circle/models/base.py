#!/usr/bin/python3
"""Create Base class"""

import json

class Base:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON representation to file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representations"""
        json_string_list = []

        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            json_string_list = json.loads(json_string)

        return json_string_list

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        # create an instance of an existing class
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
