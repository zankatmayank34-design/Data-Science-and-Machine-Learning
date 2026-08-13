def nested_exception_handling(value):
    try:
        try:
            number = int(value)
        except ValueError as e:
            print(f"Conversion error: {e}")
            number = None
        finally:
            print("Conversion attempt complete.")

        if number is not None:
            try:
                result = 10 / number
            except ZeroDivisionError as e:
                print(f"Division error: {e}")
                result = None
            finally:
                print("Division attempt complete.")

            return result
    finally:
        print("Overall execution complete.")


print(nested_exception_handling("2"))
print(nested_exception_handling("0"))
print(nested_exception_handling("a"))
