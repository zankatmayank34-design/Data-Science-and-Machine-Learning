def sum_list(values):
    total = 0

    try:
        for value in values:
            total += value
    except TypeError as e:
        print(f"Error: {e}")
        total = None
    finally:
        print("Execution complete.")

    return total


print(sum_list([1, 2, 3, 4]))
print(sum_list([1, 2, "a", 4]))
