# Uncommon Python Bug: Missed ZeroDivisionError

This repository demonstrates a subtle bug in Python related to exception handling. The `bug.py` file contains a function that attempts to handle `KeyError` and `TypeError` exceptions but fails to explicitly handle `ZeroDivisionError`. This oversight can lead to unexpected crashes and is a good example of an uncommon error that's easy to miss during testing.

The `bugSolution.py` file provides a corrected version of the function which addresses this by explicitly handling `ZeroDivisionError`.