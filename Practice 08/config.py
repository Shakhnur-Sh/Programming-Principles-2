from configparser import ConfigParser
import os


def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)

    with open(file_path, 'r', encoding='utf-8') as f:
        parser.read_file(f)

    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for key, value in params:
            config[key] = value
    else:
        raise Exception(f'Section {section} is not found in the {filename} file.')

    return config