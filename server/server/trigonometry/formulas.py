from server.task import *

import numpy as np
import yaml

def load_main_config():
    with open('config/config.yml', 'r') as file:
        return yaml.safe_load(file)


def load_trigonometry_config():
    with open('config/trigonometry.yml', 'r') as file:
        return yaml.safe_load(file)


def get_random_formula(level):
    config = load_trigonometry_config()
    formulas = config['formulas']['levels'][level]
    return np.random.choice(formulas)

def generate_task(level):
    formula = get_random_formula(level)

    task_tex = formula.split('=')[0]
    solution = formula.split('=')[1]

    return Task(task_tex, solution, level, 'Формулы')