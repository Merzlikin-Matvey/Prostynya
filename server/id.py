import datetime
from pybaseconv import Converter, BASE
import numpy as np


def generate_id():
    converter = Converter(BASE.DEC, ''.join([str(i) for i in range(10)]) + ''.join([chr(i) for i in range(65, 87)]))
    year = str(datetime.datetime.now().year)[2:]
    month = datetime.datetime.now().strftime('%b').upper()
    day = converter.convert(str(datetime.datetime.now().day))

    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second

    time = second + minute * 60 + hour * 60 * 60
    time = converter.convert(str(time)).zfill(4)

    all_symbols = ''.join([str(i) for i in range(10)]) + ''.join([chr(i) for i in range(65, 91)])
    random = np.random.choice(list(all_symbols), 4)

    return f'{year}{month}{day}{time}{random[0]}{random[1]}{random[2]}{random[3]}'
