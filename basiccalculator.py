

def add(n1, n2):
    answer = n1 + n2
    print(str(n1) + " + " + str(n2) + " = " + str(answer))

def sub(n1, n2):
    answer = n1 - n2
    print(str(n1) + " - " + str(n2) + " = " + str(answer))

def div(n1, n2):
    answer = n1  /n2
    print(str(n1) + " / " + str(n2) + " = " + str(answer))

def multi(n1, n2):
    answer = n1 * n2
    print(str(n1) + " x " + str(n2) + " = " + str(answer))

x = input('a- Adição\nb- Subtração\nc- Multiplicação\nd- Divisão\nEscolha uma função: ')

if x == 'a' or x == "A":
    print('Soma')
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    add(n1, n2)

if x == 'b' or x== "B":
    print('Subtração')
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    sub(n1, n2)

if x == 'c' or x == "C":
    print('Multiplicação')
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    multi(n1, n2)

if x == 'd' or x == "D":
    print('Divisão')
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    div(n1, n2)
