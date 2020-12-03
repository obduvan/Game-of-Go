from os.path import join
from os import path


class ConstantsPath:
    """Настройки проекта"""

    base_dir = path.dirname(__file__)  # путь проекта
    dir_graphics = join(base_dir, "../graphics")  # папка графики
