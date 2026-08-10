try:
    from mypackage import non_existent_function
except ImportError as e:
    print(f"Error importing function: {e}")
