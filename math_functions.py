import numpy as np


def create_sin_values(a, b):
    try:
        if a > b:
            print('incorrect values')
            return
        sin_array = np.sin(np.linspace(a, b, 100))
        return sin_array
    except:
        print('incorrect values')


def create_arctan_values(a, b):
    try:
        if a > b:
            print('incorrect values')
            return
        arctan_array = np.arctan(np.linspace(a, b, 100))
        return arctan_array
    except:
        print('incorrect values')


def create_exp_values(a, b):
    try:
        if a > b:
            print('incorrect values')
            return
        exp_array = np.exp(np.linspace(a, b, 100))
        return exp_array
    except:
        print('incorrect values')


def create_x_power(a, b, exp):
    try:
        if a > b:
            print('incorrect values')
            return
        power_array = np.power(np.linspace(a, b, 100), exp)
        return power_array
    except:
        print('incorrect values')


def create_diag_matrix(lst):
    return np.diag(lst)


def create_students_grades(students):
    try:
        if type(students) != str:
            if students >= 0:
                return np.array(range(int(students))), np.random.randint(100, size=int(students))
        else:
            print('incorrect values')
    except ValueError:
        print('incorrect values')


def solve(A, B):
    result = None
    try:
        result = np.linalg.solve(A, B)
    except:
        result = "Singular Matrix has det=0"
    finally:
        print(result)


def create_alpha_eye(n, alpha):
    if type(alpha) == str:
        print('incorrect values')
        return
    if type(n) == int and n > 0:
        return alpha * np.eye(n)
    else:
        print('incorrect values')
