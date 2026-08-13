def get_integer():
    try:
        value = int(input("Enter an integer: "))
    except ValueError as e:
        print(f"Error: {e}")
        value = None
    finally:
        print("Execution complete.")

    return value


print(get_integer())
