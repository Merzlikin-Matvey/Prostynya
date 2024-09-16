import numpy as np
import yaml

from server.task import *


def simplify(function, angle, sign, epsilon=10e-4):
    if function == 'sin':
        if abs(angle % np.pi) < epsilon:
            if np.sin(angle + (np.pi / 4) * sign) > 0:
                return '+', 'sin'
            else:
                return '-', 'sin'
        else:
            if np.sin(angle + (np.pi / 4) * sign) > 0:
                return '+', 'cos'
            else:
                return '-', 'cos'
    elif function == 'cos':
        if abs(angle % np.pi) < epsilon:
            if np.cos(angle + (np.pi / 4) * sign) > 0:
                return '+', 'cos'
            else:
                return '-', 'cos'
        else:
            if np.cos(angle + (np.pi / 4) * sign) > 0:
                return '+', 'sin'
            else:
                return '-', 'sin'
    elif function == 'tg':
        if abs(angle % np.pi) < epsilon:
            if np.tan(angle + (np.pi / 4) * sign) > 0:
                return '+', 'tg'
            else:
                return '-', 'tg'
        else:
            if np.tan(angle + (np.pi / 4) * sign) > 0:
                return '+', 'ctg'
            else:
                return '-', 'ctg'
    elif function == 'ctg':
        if abs(angle % np.pi) < epsilon:
            if 1 / np.tan(angle + (np.pi / 4) * sign) > 0:
                return '+', 'ctg'
            else:
                return '-', 'ctg'
        else:
            if 1 / np.tan(angle + (np.pi / 4) * sign) > 0:
                return '+', 'tg'
            else:
                return '-', 'tg'

    return None, None

def load_main_config():
    with open('config/config.yml', 'r') as file:
        return yaml.safe_load(file)


def load_trigonometry_config():
    with open('config/trigonometry.yml', 'r') as file:
        return yaml.safe_load(file)



def get_random_function(level):
    functions = load_trigonometry_config()['relationship']['levels'][level]['functions']
    return np.random.choice(functions)

def get_random_cycle(level):
    max_cycles = load_trigonometry_config()['relationship']['levels'][level]['cycles']

    cycles = np.random.randint(-max_cycles, max_cycles + 1)
    while cycles == 0:
        cycles = np.random.randint(-max_cycles, max_cycles + 1)

    if cycles % 2 == 0 and cycles > 4 and np.random.rand() < 0.6:
        return cycles - 1

    return cycles

def get_random_sign():
    return np.random.choice([-1, 1])

def generate_task(level):
    function = get_random_function(level)
    cycles = get_random_cycle(level)
    sign = get_random_sign()

    answer = simplify(function, np.pi / 2 * cycles, sign)

    if cycles % 2 == 0:
        if sign > 0:
            if cycles // 2 == 1:
                task_tex = '\\' + function + r'\left(\pi + \alpha\right)'
            elif cycles // 2 == -1:
                task_tex = '\\' + function + r'\left(-\pi + \alpha\right)'
            elif cycles < 0:
                task_tex = '\\' + function + r'\left(-' +  str(-cycles) +  r' \pi + \alpha\right)'
            else:
                task_tex = '\\' + function + r'\left(' +  str(cycles // 2) +  r' \pi + \alpha\right)'
        else:
            if cycles // 2 == 1:
                task_tex = '\\' + function + r'\left(\pi - \alpha\right)'
            elif cycles // 2 == -1:
                task_tex = '\\' + function + r'\left(-\pi - \alpha\right)'
            elif cycles < 0:
                task_tex = '\\' + function + r'\left(-' +  str(-cycles) +  r' \pi + \alpha\right)'
            else:
                task_tex = '\\' + function + r'\left(' +  str(cycles // 2) +  r' \pi - \alpha\right)'
    else:
        if sign > 0:
            if cycles == 1:
                task_tex = '\\' + function + r'\left(\dfrac{\pi}{2} + \alpha\right)'
            elif cycles == -1:
                task_tex = '\\' + function + r'\left(-\dfrac{\pi}{2} + \alpha\right)'
            elif cycles < 0:
                task_tex = '\\' + function + r'\left(-\dfrac{' +  str(-cycles) +  r' \pi}{2} + \alpha\right)'
            else:
                task_tex = '\\' + function + r'\left(\dfrac{' +  str(cycles) +  r' \pi}{2} + \alpha\right)'
        else:
            if cycles == 1:
                task_tex = '\\' + function + r'\left(\dfrac{\pi}{2} - \alpha\right)'
            elif cycles == -1:
                task_tex = '\\' + function + r'\left(-\dfrac{\pi}{2} - \alpha\right)'
            elif cycles < 0:
                task_tex = '\\' + function + r'\left(-\dfrac{' +  str(-cycles) +  r' \pi}{2} - \alpha\right)'
            else:
                task_tex = '\\' + function + r'\left(\dfrac{' +  str(cycles) +  r' \pi}{2} - \alpha\right)'


    answer_tex = ''
    if answer[0] == '-':
        answer_tex += '-'


    answer_tex += '\\' + answer[1] + r'{\alpha}'

    return Task(
        task_tex,
        answer_tex,
        level,
        'Формулы приведения',
    )


