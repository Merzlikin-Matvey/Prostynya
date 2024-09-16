import shutil
import yaml
import os

def copy_and_rename_template(id):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    config_path = os.path.join(project_root, 'config', 'config.yml')
    solution = 'solution' in id
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        if not solution:
            template_path = config['trigonometry_template_path']
        else:
            template_path = config['trigonometry_solutions_template_path']

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    src = os.path.join(project_root, template_path)
    dst_dir = os.path.join(project_root, 'files')
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.join(dst_dir, f'{id}.tex')
    shutil.copy(src, dst)

def edit_file(data, id):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    file_path = os.path.join(project_root, 'files', f'{id}.tex')

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for key, value in data.items():
        placeholder = f'{{{{ {key} }}}}'
        content = content.replace(placeholder, value)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
