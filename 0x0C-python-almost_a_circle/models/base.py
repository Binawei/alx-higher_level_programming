#!/usr/bin/python3
"""
This module is about the base class for all other tasks of this projects
to manage id attribute in all your future classes and to avoid duplicating the
same code (by extension, same bugs)
"""
import json
class Base:
    """
    A base class to manage ID attribute of subclasses to avoid code duplication
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding="utf-8") as a_file:
            obj_list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(obj_list)
            a_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(**dictionary):
        """Returns an instance with all attributes already set
        args:
            -dictionary: a double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        elif cls.__name__ == "Square":
            new_obj = cls(1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ +".json"
        try:
            with open(filename, mode='r', encoding="utf-8") as a_file
                json_string = a_file.read()
                obj_list = cls.from_json_string(json_string)
                return [cls.create(**dictionary) for dictionary in obj_list]
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This method writes an object in the provided list_objs to a CSV file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', encoding="utf-8") as a_file:
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    a_file.write("{},{},{},{},{}\n".format(obj.id, obj.width, obj.height, obj.x, obj.y))
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    a_file.write("{},{},{},{}\n".format(obj.id, obj.size, obj.x, obj.y))
    

    @classmethod
    def load_from_file_csv(cls):
        """loads file from a CSV file as oppose to he above"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r' encoding="utf-8") as a_file:
                list_objs = []
                for line in a_file:
                    attributes = line.split(",")
                    if cls.__name__ == "Rectangle":
                        obj = cls(int(attributes[1]), int(attributes[2]), int(attributes[3]), int(attributes[4]), int(attributes[0]))
                    elif cls.__name__ == "Square":
                        obj = cls(int(attributes[1]), int(attributes[2]), int(attributes[3]))
                    list_objs.append(obj)
                return list_objs
        except FileNotFoundError:
            return []
