class ValidateInputTime:
    @staticmethod
    def validate_time(time_1, time_2):
        try:
            time_1 = int(time_1)
            time_2 = int(time_2)
        except TypeError:
            return False
        except Exception:
            return False
        else:
            if isinstance(time_1, int) and isinstance(time_2, int) and (time_1 >= 0 and time_2 >= 0):
                return time_1 > 0 or time_2 > 0
            return False
