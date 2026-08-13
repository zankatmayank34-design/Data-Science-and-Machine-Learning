def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        result = None
    finally:
        print("Execution complete.")
    return result


print(divide(10, 2))
print(divide(10, 0))
