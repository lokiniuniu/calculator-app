def validate_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def format_result(result):
    return f"The result is: {result}"