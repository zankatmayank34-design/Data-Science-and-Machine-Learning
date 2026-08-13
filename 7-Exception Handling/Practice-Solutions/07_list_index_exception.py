def get_list_element(values, index):
    try:
        element = values[index]
    except IndexError as e:
        print(f"Error: {e}")
        element = None
    finally:
        print("Execution complete.")

    return element


numbers = [1, 2, 3, 4, 5]

print(get_list_element(numbers, 2))
print(get_list_element(numbers, 10))
