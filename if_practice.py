"""
My practice for if then else loop
"""
import os,sys,time
import re
import math
FACTOR = 10

class compare():
    def check_num_greater_than_four(self, num):
        if num > 4:
            print(f'{num} is greater than 4')
        else:
            print(f'{num } is less than 4')

def f(y):
    ''' compute the square of y '''
    return (y*y)

def printName(first, last, onlyLast=False):

    if onlyLast:
        print (last)
    else:
        print (first, last)

def printapp(f, xs):
    for i in xs:
        print(f(i), end='%')

def double(x):
    return x+x



def sieve(n):

    global primes
    primes = [True]*(n+1)
    primes[0], primes[1]= False, False

    for j in range(2, n+1):
        if primes[j] == False:
            continue

    for i in range(j*j, n+1, j+1):
        primes[i] == False

def f(n):
    i = 2
    while i*i < n :
        if (n%i) == 0:
            return i
        i = i + 1
    return n

class Person:
    def getInfo(self):
        return "Person's getInfo is called"

    def printPerson(self):
        print(self.getInfo())

class Staff(Person):
    def getInfo(self):
        return "Staff's getInfo is called"

def main():
    Person().printPerson()
    Staff().printPerson()

def serach(a, start, end, key):

    if start > end:
        return False
    if a[start] == key:
        return True
    return search(a, start+1, end, key)

def search_mid(a, start, end, key):
    if start > end:
        return False
    mid = start + end // 2

    if a[mid] == key:
        return True

    return search(a, mid+1, end, key) or serach(a, mid+1, end, key)

def binsearch(a, start, end, key):

    if start > end:
        return False
    mid = start + end // 2

    if a[mid] == key:
        return True

    if a[mid] >= key:
        return binsearch(a, start, mid-1, key)
    else:
        return binsearch(a, mid+1, end, key)

def fff(n):
    if n <= 1:
        return n
    else:
        return fff(n-1) + fff(n-2)

def hanoi(n, A, C, B):
    if n == 0:
        return True
    hanoi(n-1, A, B, C)
    print("move 1 disk from %s to %d", (A, B))
    hanoi(n-1, B, C, A)

def selection_sort(a, start, end, comp):
    if start == end:
        return True

    idx_max = find_idx_of_max_elt(a, start, end, comp)
    a[idx_max], a[start] = a[start], a[idx_max]
    selection_sort(a, start+1, end, comp)

def find_idx_of_max_elt(a:list, start:int, end:int, comp) -> int:
    start = 0
    max = start
    for i in range(start, end):
        if (comp(a[i], a[max])):
            max = i

    return max

def sort(a, comp):

    selection_sort(a, 0, len(a), comp)
    return True

def intgt(x, y):
    return x > y
def intlt(x, y):
    return x < y
def namecmp(t1, t2):
    return t1[0] < t2[0]
def agecmp(t1, t2):
    return t1[1] < t2[1]

"""
def merge(ar, start, n):

    i, lim i = a, start+n/2
    j, lim j = start+n/2, n

    temp = []

    while (i < lim_i) and (j < lim j):
        if (ar[i] <= ar[j]):
            temp.append(ar[i])
            i = i + 1
        else:
            temp. append(ar[j])
            j = j + 1

    while (j < lim_j):
        temp.append(ar[j])
        j = j + 1

    while (i < lim_i):
        temp.append(ar[i])
        i = i + 1

    for k in range(n):
        ar[start + k] = temp [k]

def merge_sort(ar, start, n):
    if (n > 1):
        half = n // 2
        merge_sort(ar, start, half)
        merge_sort(ar, start+half, n-half)
        merge(ar, start, n)

def sort_by_merge(a):
    merge_sort(a, 0, len(a))
"""

def func():
    global x
    print('x is', x)
    x = 4
    print('Changed global x to', x)

def h():
    pass

class A:
    def __init__(self, i = 0, j = 0):
        self.i = i
        self.j = j

    def __str__(self):
        return "some string"

    def __eq__(self, other):
        return self.i % self.j == other.i % other.j

def main():
    x = A(4, 3)
    y = A(6, 2)
    print(x == y)

def xyz(i = 4, j = 3):
    i = i + j
    j = j + 1
    print(i, j)

def fn(a,b):
    v=1
    b[0]=100


a = [17, 82, 35]
b = [8, 95, 55]

result= []

def compareTriplets(a, b):
    total_a = 0
    total_b = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            total_a = total_a + 1
        elif a[i] < b[i]:
            total_b = total_b + 1

    return (total_a, total_b)

ar = [1,2,3, 4,5]

def aVeryBigSum(ar):
    sum = 0

    for i in ar:
        sum += i

    return sum


#---START OF SCRIPT
if __name__=='__main__':


    print(a)
    print(b)
    print(compareTriplets(a, b))
    print(aVeryBigSum(ar))
