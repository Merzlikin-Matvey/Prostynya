import typing
from server.trigonometry.calculations import generate_task as generate_calculation_task
from server.trigonometry.relationship import generate_task as generate_relationship_task
from server.trigonometry.formulas import generate_task as generate_formula_task
from server.task import Task
from .configs import load_trigonometry_config
import numpy as np


def generate_trigonometry_tasks(
        calculations: int = 2,
        relationships: int = 2,
        formulas: int = 2,
        level: int = 5,
        radians: bool = True
) -> typing.List[Task]:
    config = load_trigonometry_config()
    calculations_probs = config['probabilities']['calculations']['levels'][level]
    relationships_probs = config['probabilities']['relationships']['levels'][level]
    formulas_probs = config['probabilities']['formulas']['levels'][level]
    tasks = []

    for i in range(calculations):
        current_level = np.random.choice([1, 2, 3, 4, 5], p=calculations_probs)
        task = generate_calculation_task(level=current_level, radians=radians)
        tasks.append(task)

    for i in range(relationships):
        current_level = np.random.choice([1, 2, 3, 4, 5], p=relationships_probs)
        task = generate_relationship_task(level=current_level, radians=radians)
        tasks.append(task)

    for i in range(formulas):
        current_level = np.random.choice([1, 2, 3, 4, 5], p=formulas_probs)
        task = generate_formula_task(level=current_level)
        tasks.append(task)

    np.random.shuffle(tasks)

    print('tasks_generated')
    return tasks
