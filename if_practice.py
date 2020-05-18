"""
My practice for if then else loop
"""
import os,sys,time,pytest

class compare():
    def check_num_greater_than_four(self, num):
        if num > 4:
            print(f'{num} is greater than 4')
        else:
            print(f'{num } is less than 4')
#---START OF SCRIPT
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    compare_obj = compare()
    # checkin number greater than four
    compare_obj.check_num_greater_than_four(5)
    # checkin number less than four
    compare_obj.check_num_greater_than_four(3)
else:
        print('ERROR: Received incorrect comand line input arguments')