from math import radians

from flask import Flask, request, jsonify, send_file, send_from_directory
from .create_files import generate_trigonometry_files
from .id import generate_id
from .render import render_tex_file
import os

app = Flask(__name__, static_folder='../dist', static_url_path='')

@app.route('/')
def serve_vue_app():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/trigonometry', endpoint='serve_trigonometry')
def serve_vue_app():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/generate_trigonometry', methods=['POST'])
def generate():
    print('Generating trigonometry dictation')
    data = request.json
    title = data.get('title', 'Диктант')
    grading_system = data.get('grading_system_name', 'Всем 2!')
    num_calculations = data.get('num_calculations', 2)
    num_relationships = data.get('num_relationships', 2)
    num_formulas = data.get('num_formulas', 2)
    difficulty = data.get('difficulty', 4)
    radians = data.get('radians', True)

    num_calculations = num_calculations if num_calculations is not None else 0
    num_relationships = num_relationships if num_relationships is not None else 0
    num_formulas = num_formulas if num_formulas is not None else 0


    num = num_calculations + num_relationships + num_formulas
    if num > 239:
        num_calculations = 80
        num_relationships = 80
        num_formulas = 80


    if not isinstance(difficulty, int) or difficulty < 1 or difficulty > 5:
        difficulty = 4

    if len(title) < 1 or len(title) > 100 or title == ' ':
        title = 'Диктант'

    if len(grading_system) < 2 or not grading_system:
        grading_system = 'Всем 2!'

    id = generate_id()
    paths = generate_trigonometry_files(
        id=id,
        num_calculations=num_calculations,
        num_relationships=num_relationships,
        num_formulas=num_formulas,
        level=difficulty,
        title=title,
        rating=grading_system,
        radians=radians
    )
    for path in paths:
        render_tex_file(path)

    print("Отправка")
    return jsonify({'id': id})

@app.route('/download/<file_id>', methods=['GET'])
def download(file_id):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    file_path = os.path.join(project_root, '..', 'files', f'{file_id}.pdf')
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({'error': 'File not found'}), 404




