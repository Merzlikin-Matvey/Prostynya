import server.trigonometry.trigonometry as trigonometry
from server.generate_tex_template import copy_and_rename_template, edit_file
import os


def generate_trigonometry_files(
        id: str,
        num: int,
        level: int,
        title: str = 'Диктант',
        rating: str = 'Всем 2!'
):
    copy_and_rename_template(id)
    copy_and_rename_template(f'{id}_solutions')

    tasks = trigonometry.generate_trigonometry_tasks(num, level)
    tasks_latex = ''
    solutions_latex = ''
    for i, task in enumerate(tasks):
        tasks_latex += f'\\item \\begin{{tabularx}}{{\\linewidth}}{{@{{}}l X@{{}}}}${task.task}=$ & \\hrulefill \\end{{tabularx}}\n'
        if task.defined:
            solutions_latex += f'\\item ${task.task} = {task.answer}$\n'
        else:
            solutions_latex += f'\\item ${task.task}$ Не определено!\n'

    data = {
        "tasks": tasks_latex,
        "title": title,
        "rating": rating,
        "id": id
    }
    edit_file(data, id)

    solutions_data = {
        "solutions": solutions_latex,
        "title": f'{title} - Ответы',
        "rating": rating,
        "id": id,
    }
    edit_file(solutions_data, f'{id}_solutions')

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    tex_file_path = os.path.join(project_root, 'files', f'{id}.tex')
    solutions_tex_file_path = os.path.join(project_root, 'files', f'{id}_solutions.tex')

    return tex_file_path, solutions_tex_file_path