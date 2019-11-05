# Module for main logic of the app

import math
from os.path import dirname

import numpy as np
from sklearn.datasets.base import load_data


def entropy_formula(class_number, group_number):
    return -(class_number*1.0/group_number) * \
           math.log2(class_number*1.0/group_number)

def entropy_cal(c1, c2):
    """
    Returns entropy of a group of data
    c1: count of one class
    c2: count of another class
    """
    if c1== 0 or c2 == 0:  # when there is only one class in the group, entropy is 0
        return 0
    return entropy_func(c1, c1+c2) + entropy_func(c2, c1+c2)