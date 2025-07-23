first = int(input("Erste Zahl: "))
operator = input("Rechenoperator: ")
second = int(input("Zweite Zahl: "))
'''
if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    print(first / second)
else:
    print("Nur + - * / sind zulässig")
'''
match operator:
    case '+':
        print(first + second)
    case '-':
        print(first - second)
    case '*':
        print(first * second)
    case '/':
        print(first / second)
    case _:
        print("Nur + - * / zulässig!")