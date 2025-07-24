eingabe = input("Eingabe... ")
rechnung = eingabe.replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("/", " / ")
ergebnis = 0
liste = rechnung.split()

if any(x == '+' or x == '-' or x == '*' or  x == '/' for x in liste):
    match liste[1]:
        case '+':
            ergebnis = float(liste[0]) + float(liste[2])
            print(ergebnis)
        case '-':
            ergebnis = float(liste[0]) - float(liste[2])
            print(ergebnis)
        case '*':
            ergebnis = float(liste[0]) * float(liste[2])
            print(ergebnis)
        case '/':
            ergebnis = float(liste[0]) + float(liste[2])
            print(ergebnis)
else:
    print("Kein zugelassener Operator + - * /")