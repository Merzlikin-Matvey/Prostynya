import typing
from server.trigonometry.calculations import generate_task as generate_calculation_task
from server.trigonometry.relationship import generate_task as generate_relationship_task
from server.trigonometry.formulas import generate_task as generate_formula_task
from server.task import Task
import numpy as np

def generate_trigonometry_tasks(num: int = 5, level: int = 3,  probs=None) -> typing.List[Task]:
    if probs is None:
        probs = [1/3, 1/3, 1/3]

    tasks = []
    for i in range(num):
        task_type = np.random.choice(['calculation', 'relationship', 'formulas'], p=probs)
        if task_type == 'calculation':
            task = generate_calculation_task(level)
        elif task_type == 'relationship':
            task = generate_relationship_task(level)
        elif task_type == 'formulas':
            task = generate_formula_task(level)
        tasks.append(task)
    return tasks