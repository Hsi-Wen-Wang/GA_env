from enum import Enum

class WorkCost:
    time = 0

class Type(Enum):
    NONE = 0
    A = 1
    B = 2

class Process(Type, Enum):
    ID = 0



class test:
    test_num = 0

A = Process()

print(A.ID)
