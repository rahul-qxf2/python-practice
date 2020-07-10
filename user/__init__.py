"""
https://pypi.org/project/dacite/
https://github.com/Dobiasd/undictify
https://stackoverflow.com/questions/35282222/in-python-how-do-i-cast-a-class-object-to-a-dict/35282286


"""

from dataclasses import dataclass, asdict, field, InitVar

@dataclass
class User(object):
    name: str
    age: int
    is_active: bool