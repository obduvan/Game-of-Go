class ValidateInputTime:
    @staticmethod
    def validate_time(time_1, time_2):
        try:
            print(time_1, time_2)
            time_1 = int(time_1)
            time_2 = int(time_2)
        except TypeError:
            return False
        except Exception:
            return False
        else:

            return isinstance(time_1, int) and isinstance(time_2, int) and (time_1 > 0 or time_2 > 0)
