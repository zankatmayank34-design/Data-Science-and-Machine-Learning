def get_dict_value(data, key):
    try:
        value = data[key]
    except KeyError as e:
        print(f"Error: {e}")
        value = None
    finally:
        print("Execution complete.")

    return value


data = {"a": 1, "b": 2, "c": 3}

print(get_dict_value(data, "b"))
print(get_dict_value(data, "x"))
