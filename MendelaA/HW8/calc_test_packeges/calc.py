import defs

val1 = int(input('Input first num '))
val2 = int(input('Input second number '))
action = input('Input action ')

# if action == '-':
#     print(defs.minus(val1, val2))
# elif action == '+':
#     print(defs.plus(val1, val2))
# elif action == '*':
#     print(defs.multiply(val1, val2))
# elif action == '/':
#     print(defs.divide(val1, val2))

# Try to use Case
match action:
    case '-':
        print(defs.minus(val1, val2))
    case '+':
        print(defs.plus(val1, val2))
    case '*':
        print(defs.multiply(val1, val2))
    case '/':
        print(defs.divide(val1, val2))
