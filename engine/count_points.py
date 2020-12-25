class CountPoints:
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def _count_points(self, groups):
        points = 0
        for group in groups:
            points += len(group)
        return points

    def count_points_black(self, black_groups):
        return self._count_points(black_groups)

    def count_points_white(self, white_groups):
        return self._count_points(white_groups)
