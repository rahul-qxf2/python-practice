"""
https://pypi.org/project/dacite/
https://github.com/Dobiasd/undictify
https://stackoverflow.com/questions/35282222/in-python-how-do-i-cast-a-class-object-to-a-dict/35282286


"""

from user_helper import UserHelper

#----START OF SCRIPT
if __name__=='__main__':

    print("Test start")
    user = UserHelper()
    user_dict = user.get_dict('John','40','True')
    print(user_dict)
    print(type(user_dict))