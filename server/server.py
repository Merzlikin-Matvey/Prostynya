from flask import Flask, request, jsonify, send_file
from server.create_files import generate_trigonometry_files
from server.id import generate_id
from server.render import render_tex_file
import os

app = Flask(__name__)

@app.route('/generate_trigonometry', methods=['POST'])
def generate():
    data = request.json
    title = data.get('title', 'Диктант')
    grading_system = data.get('grading_system', 'default')
    num_tasks = data.get('num_tasks', 10)
    difficulty = data.get('difficulty', 1)

    id = generate_id()
    paths = generate_trigonometry_files(id, num_tasks, difficulty, title=title)
    for path in paths:
        render_tex_file(path)

    return jsonify({'id': id})

@app.route('/download/<file_id>', methods=['GET'])
def download(file_id):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    file_path = os.path.join(project_root, 'files', f'{file_id}.pdf')
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)