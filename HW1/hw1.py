def divide_by_zero():
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: Division by zero")
        
def type_error():
    try:
        result = "10" + 20
    except TypeError:
        print("Error: Type mismatch")

def value_error():
    try:
        number = int("abc")
    except ValueError:
        print("Error: Invalid value")

def system_exit():
    try:
        sys.exit("Exiting the program")
    except SystemExit:
        print("Error: System exit")

value_error()