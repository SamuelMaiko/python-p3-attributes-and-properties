#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __ini__(self):
        self._new_name=""
        self._breed=""
    def get_name(self):
        return self._new_name
    def set_name(self, new_name):
        if new_name=="":
            print("Name must be string between 1 and 25 characters.")
        elif type(new_name) is str and 1<=new_name<=25:
            self._new_name=new_name
        else:
            print("Name must be string between 1 and 25 characters.")


    name=property(get_name, set_name)

    def get_breed(self):
        return self._breed
    def set_breed(self,breed):
        if breed in APPROVED_BREEDS:
            self._breed=breed
        else:
            print("Breed must be in list of approved breeds.")

    breed=property(get_breed, set_breed)
