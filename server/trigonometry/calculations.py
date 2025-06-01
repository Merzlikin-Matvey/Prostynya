import random
import re

import numpy as np

from server.task import Task
from server.trigonometry.configs import *

FUNCTIONS = {
    'sin': np.sin,
    'cos': np.cos,
    'tg': np.tan,
    'ctg': lambda x: 1 / np.tan(x)
}

VALUES = {
    0: '0',
    np.sin(np.pi / 6): r'\dfrac{1}{2}',
    np.sin(np.pi / 4): r'\dfrac{\sqrt{2}}{2}',
    np.sin(np.pi / 3): r'\dfrac{\sqrt{3}}{2}',
    np.sin(np.pi / 2): '1',
    np.cos(np.pi / 6): r'\dfrac{\sqrt{3}}{2}',
    np.cos(np.pi / 4): r'\dfrac{\sqrt{2}}{2}',
    np.cos(np.pi / 3): r'\dfrac{1}{2}',
    np.tan(np.pi / 6): r'\dfrac{\sqrt{3}}{3}',
    np.tan(np.pi / 3): r'\sqrt{3}',
}


def get_random_function_and_angle(level: int = 1):
    trigonometry_config = load_trigonometry_config()

    level_config = trigonometry_config['calculations']['levels'][level]
    functions = level_config['functions']
    angles = level_config['angles']
    negative = level_config['negative']

    random_function = random.choice(functions)
    random_angle = random.choice(angles)

    if negative:
        if (np.random.rand() < 0.5):
            random_angle = f'-{random_angle}'

    return random_function, random_angle


def convert_tex_angle_to_number(angle: str):
    angle = re.sub(r'(\d)\s*(\\pi)', r'\1*\2', angle)
    angle = angle.replace(r'\pi', str(np.pi))

    if r'\dfrac' in angle:
        angle = angle.replace(r'\dfrac{', '')
        angle = angle.split('}{')
        angle[1] = angle[1].replace('}', '')
        return eval(angle[0]) / eval(angle[1])
    else:
        return float(angle)


def get_value(function: str, angle: str):
    angle = convert_tex_angle_to_number(angle)
    return FUNCTIONS[function](angle)


def convert_number_to_tex(number, epsilon=0.0001, inf=10e8):
    if number > inf or number < -inf:
        return np.inf

    for (key, value) in VALUES.items():
        if abs(key - number) < epsilon:
            return value
        if abs(-key - number) < epsilon:
            return f'-{value}'

    raise ValueError(f'Value {number} is not a standard value')


def is_negative(angle: str):
    return '-' in angle


def rad_to_deg(angle):
    value = convert_tex_angle_to_number(angle)
    return round(value / np.pi * 180)


def deg_to_tex(deg_value):
    return str(deg_value) + r'^{\circ}'


def generate_task(level: int = 1, radians: bool = 1):
    function, angle = get_random_function_and_angle(level)
    value = get_value(function, angle)
    if radians:
        tex_angle = angle.replace('*', r'\cdot ')
    else:
        tex_angle = deg_to_tex(rad_to_deg(angle))
    tex_value = convert_number_to_tex(value)

    if not is_negative(angle):
        tex_task = '\\' + function + '{' + tex_angle + '}'
    else:
        tex_task = '\\' + function + r'{\left(' + tex_angle + r'\right)}'

    return Task(tex_task, tex_value, level, 'Тригонометрия. Вычисления', defined=(tex_value != np.inf))
