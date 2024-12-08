def function_with_uncommon_error(data):
    try:
        result = 10 / data['value']  # Potential ZeroDivisionError
        return result
    except KeyError:
        return 0  # Handling KeyError, but ZeroDivisionError might be missed
    except TypeError:
        return -1  # Handling TypeError, but ZeroDivisionError might be missed

# Example usage that might trigger the bug
data = {'value': 0}
print(function_with_uncommon_error(data)) # Raises ZeroDivisionError
data = {'key': 'value'}
print(function_with_uncommon_error(data)) # Returns 0
data = 10
print(function_with_uncommon_error(data)) # Raises TypeError