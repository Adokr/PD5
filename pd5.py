kod1 = {'G': 'A', 'A': 'G', 'D': 'E', 'E': 'D', 'R': 'Y', 'Y': 'R',
        'P': 'O', 'O': 'P', 'L': 'U', 'U': 'L', 'K': 'I', 'I': 'K'}
kod2 = {'P': 'O', 'O': 'P', 'L': 'I', 'I': 'L', 'T': 'Y', 'Y': 'T',
        'K': 'A', 'A': 'K', 'R': 'E', 'E': 'R', 'N': 'U', 'U': 'N'}

def encrypt(x, y):
    wynik = ''
    if y == '1':
        for i in x:
            if i.upper() in kod1.keys():
                wynik += kod1.get(i.upper())
            else:
                wynik += i.upper()
    elif y == '2':
        for i in x:
            if i.upper() in kod2.keys():
                wynik += kod2.get(i.upper())
            else:
                wynik += i.upper()
    else:
        for i in x:
            if i.upper() in kod3.keys():
                wynik += kod3.get(i.upper())
            else:
                wynik += i.upper()
    return wynik

def defineNewCode(x):
    czyJednoznaczny = True
    y = []
    szyfr = {}
    for i in range(0, len(x), 2):
         y.append(x[i:i+2])

    for i in y:
        if i[0].upper() in szyfr.keys() or i[1].upper() in szyfr.keys():
            czyJednoznaczny = False
        szyfr.update({i[0].upper(): i[1].upper(), i[1].upper(): i[0].upper()})

    return szyfr, czyJednoznaczny

whichCode = input("Wybierz szyfr, którego chcesz użyć:\n(1) - GA-DE-RY-PO-LU-KI\n(2) - PO-LI-TY-KA-RE-NU\n(3) - własny szyfr\n")
assert whichCode == '1' or whichCode == '2' or whichCode == '3', "Niepoprawna komenda"

if whichCode == '3':
    code = "o"
    while len(code) % 2 != 0:
        code = input("Podaj szyfr, którego chcesz użyć (format: XYZWABPR)\n")

    kod3 = defineNewCode(code)[0]
    print(kod3)
    if defineNewCode(code)[1]:
        print("Podany szyfr jest jednoznaczy\n")
    else:
        print("Podany szyfr nie jest jednoznanczy\n")

action = input("Wybierz co chcesz zrobić:\n(z) - zakodować wiadomość\n(o) - odkodować wiadomość\n")
assert action == 'z' or action == 'o', "Niepoprawna komenda"

if action == 'o':
    message = input("Podaj wiadomość, którą chcesz odszyfrować\n")
    print(encrypt(message, whichCode))
else:
    message = input("Podaj wiadomość, którą chcesz zaszyfrować\n")
    print(encrypt(message, whichCode))
