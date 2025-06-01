import subprocess
import os


def render_tex_file(filename):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    output_dir = os.path.join(project_root, 'files')

    os.makedirs(output_dir, exist_ok=True)

    result = subprocess.run(['pdflatex', '-output-directory', output_dir, filename], capture_output=True, text=True,
                            errors='ignore')
    if result.returncode != 0:
        print(f"Error rendering {filename}: {result.stderr}")
    else:
        print(f"Successfully rendered {filename}")
