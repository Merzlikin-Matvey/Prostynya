from server.task import *

import numpy as np
import yaml
import os

from server.trigonometry.configs import *


def get_random_formula(level):
    config = load_trigonometry_config()
    formulas = config['formulas']['levels'][level]
    return np.random.choice(formulas)

def generate_task(level):
    formula = get_random_formula(level)

    task_tex = formula.split('=')[0]
    solution = formula.split('=')[1]

    return Task(task_tex, solution, level, 'Формулы')