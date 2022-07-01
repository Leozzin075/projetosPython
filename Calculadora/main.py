import functions

opcao = str(input('Escolha qual das operaçoes voce quer fazer:\n A) Soma\n B) Subtracao\n C) Multiplicacao\n D) Divisao\n Digite a opçao desejada:\n -->'))
if opcao == 'A' or opcao == 'a':
    valor1 = float(input('Digite o primeiro valor desejado:\n -->'))
    valor2 = float(input('Digite o segundo valor desejado:\n -->'))
    resultado = functions.soma(valor1, valor2)
    print(f'O resultado da soma {valor1} + {valor2} é igual a: {resultado}')
elif opcao == 'B' or opcao == 'b':
    valor1 = float(input('Digite o primeiro valor desejado:\n -->'))
    valor2 = float(input('Digite o segundo valor desejado:\n -->'))
    resultado = functions.subtra(valor1, valor2)
    print(f'O resultado da subtraçao {valor1} - {valor2} é igual a: {resultado}')
elif opcao == 'C' or opcao == 'c':
    valor1 = float(input('Digite o primeiro valor desejado:\n -->'))
    valor2 = float(input('Digite o segundo valor desejado:\n -->'))
    resultado = functions.multi(valor1, valor2)
    print(f'O resultado da multiplicaçao {valor1} x {valor2} é igual a: {resultado}')
elif opcao == 'D' or opcao == 'd':
    valor1 = float(input('Digite o primeiro valor desejado:\n -->'))
    valor2 = float(input('Digite o segundo valor desejado:\n -->'))
    resultado = functions.dividir(valor1, valor2)
    print(f'O resultado da divisao {valor1} / {valor2} é igual a: {resultado}')
else:
    print('error...')