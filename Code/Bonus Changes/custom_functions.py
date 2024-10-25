def custom_functions(func_name, *args):
    functions = {
        "calculate_bonus": calculate_bonus,
        # Add more custom functions here
    }
    return functions.get(func_name)(*args) if func_name in functions else None

def calculate_bonus(experience, salary):
    return salary * 0.1 if experience > 5 else 0
