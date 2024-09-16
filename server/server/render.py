import subprocess
import os


def render_tex_file(tex_file_path: str):
    directory, filename = os.path.split(tex_file_path)

    os.chdir(directory)

    result = subprocess.run(['pdflatex', filename], capture_output=True, text=True)

    if result.returncode != 0:
        print("Error rendering the .tex file:")
        print(result.stderr)
    else:
        print("Successfully rendered the .tex file to PDF.")