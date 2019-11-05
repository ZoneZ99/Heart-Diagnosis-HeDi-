# Module for main logic of the app

import math
from os.path import dirname

import numpy as np
from sklearn.datasets.base import load_data


def entropy_formula(class_number, group_number):
    return -(class_number*1.0/group_number) * math.log2(class_number*1.0/group_number)


def entropy_calculation(class1,class2):
    group_number = class1 +class2
    if class1 > 0  and class2 >0:
        return entropy_formula(class1, group_number)+entropy_formula(class2,group_number)
    return 0

def entropy_one_division(division):
    sum_entropy = 0
    num_of_division = len(division)
    classess = set(division)

    for clas in classes:
        sum_entropy += sum(division == clas)*1.0/num_of_divission * entropy_calculation(sum(division == clas ),sum(division != clas))
    return sum_entropy, num_of_division

