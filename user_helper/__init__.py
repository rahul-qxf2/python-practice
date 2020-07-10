"""
https://pypi.org/project/dacite/
https://github.com/Dobiasd/undictify
https://stackoverflow.com/questions/35282222/in-python-how-do-i-cast-a-class-object-to-a-dict/35282286


"""

from dataclasses import dataclass, asdict, field, InitVar
from user import User

class UserHelper(object):


    def __init__(self):

        pass

    def get_dict(self,name,age,is_active):

        self.name = name
        self.age = age
        self.is_active = is_active

        sample_dict = asdict(User(self.name,self.age,self.is_active))

        return sample_dict
