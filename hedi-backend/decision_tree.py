# Module for main logic of the app

import math
from os.path import dirname

import numpy as np
from sklearn.datasets.base import load_data


def entropy_formula(class_number, group_number):
    return -(class_number*1.0/group_number) \ math.log2(class_number*1.0/group_number)


def entropy_calculation(class1,class2):
    group_number = class1 +class2
    if class1 > 0  and class2 >0:
        return entropy_formula(class1, group_number)+entropy_formula(class2,group_number)
    return 0

