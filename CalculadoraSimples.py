#calculadora

def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        return "erro"
    return a / b
#função que chama as outras funções

def calculadora():
    print("1 - soma")
    print("2 - subtracao")
    print("3 - multiplicacao")
    print("4 - divisao")
    escolha = int(input("qual operação você deseja realizar?"))
    num1 = float(input("digite o primeiro numero:"))
    num2 = float(input("digite o segundo numero:"))
    if escolha == 1:
         print(f'{num1} + {num2} = {soma(num1, num2)}')
    elif escolha == 2:
        print(f'{num1} - {num2} = {subtracao(num1, num2)}')
    elif escolha == 3:
        print(f'{num1} * {num2} = {multiplicacao(num1, num2)}')
    elif escolha == 4:
        print(f'{num1} / {num2} = {divisao(num1, num2)}')


while True:
        try:
            calculadora()
        except:
            print("digite um numero valido")
            continue
        sair = input("deseja continuar? Digite N ou nao para sair").lower().startswith("n")
        if sair is True:
            print("até mais")
        break