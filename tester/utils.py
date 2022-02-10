"""
Utility functions for CS2900 Lab 3 checkpoint test suite.

Author: Tom Kuipers
"""
import numpy as np

def check_code(regex):
    import inspect
    import re
    local_vars = str(inspect.currentframe().f_back.f_back.f_locals)
    no_match = len(re.findall(regex, local_vars)) == 0
    return no_match


def check_As(As):
    conj = True
    for i in range(4):
        Ai = np.load(f"tester/res/A{i}.npy")
        conj = conj and np.allclose(As[i], Ai, atol=10**-3, rtol=0)
    return conj


def check_bs(bs):
    conj = True
    for i in range(4):
        bi = np.load(f"tester/res/b{i}.npy")
        conj = conj and np.array_equal(bs[i], bi)
    return conj

def check_array_list(name, list):
    conj = True
    for i in range(len(list)):
        exp = np.load(f"tester/res/{name}{i}.npy")
        conj = conj and np.array_equal(list[i], exp)
    return conj