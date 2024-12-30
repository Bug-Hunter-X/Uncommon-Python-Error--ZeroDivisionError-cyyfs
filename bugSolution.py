def function_with_uncommon_error(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a + b
    except ZeroDivisionError as e:
        print("Error:", e)
        return None  # Or handle the error appropriately