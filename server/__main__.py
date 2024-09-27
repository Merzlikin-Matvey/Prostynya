from .server import app
from .trigonometry.trigonometry import *

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
