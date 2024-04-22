

def validate_number(num):
    if isinstance(num, int) or isinstance(num, float):
        return num
    return False