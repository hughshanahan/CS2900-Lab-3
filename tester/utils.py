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


def check_array_list(fname, list):
    for i in range(len(list)):
        exp = np.load(f"tester/res/{fname}{i}.npy")
        if not np.array_equal(list[i], exp):
            print(f"{fname}[{i}] is not incorrect! Double check this value.")
            return False
    return True

