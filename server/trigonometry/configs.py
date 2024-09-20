import os
import yaml

def load_main_config():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    config_path = os.path.join(project_root, 'config', 'config.yml')

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    return config

def load_trigonometry_config():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    config_path = os.path.join(project_root, 'config', 'trigonometry.yml')

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    return config