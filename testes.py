print('---------------------Bem vindo a nossa lanchonete virtual----------------------')
try:
    A = int(input('Deseja ver nosso cardápio:\n1. Sim\n2. Não\n-->'))
except:
    print('Digite apenas 1 ou 2 para prosseguir')
    A = int(input('Deseja ver nosso cardápio:\n1. Sim\n2. Não\n-->'))


match (A):
    case 1:
        print('1. coxinha R$ 5,00\n2. Pastel R$ 7,00\n3. Café R$ 4,00\n4. Suco R$ 6,00\n5. Sair ')
        total = 0

        while (True):
            try:
                op = int(input('Qual item quer comprar?: '))   
            except:
                print('A resposta deve contar apenas números')
                continue

            match (op):
                case 1:
                    qtd = int(input('Quantas unidades quer comprar?: '))
                    total = 5.00 * qtd
                    print(f'total = R$ {total}')
                case 2:
                    qtd = int(input('Quantas unidades quer comprar?: '))
                    total = 7.00 * qtd
                    print(f'total = R$ {total}')
                case 3:
                    qtd = int(input('Quantas unidades quer comprar?: '))
                    total = 4.00 * qtd
                    print(f'total = R$ {total}')
                case 4:
                    qtd = int(input('Quantas unidades quer comprar?: '))
                    total = 6.00 * qtd
                    print(f'total = R$ {total}')
                case 5:
                    break
                case _:
                    print('O valor deve estar entre uma das opções')
                    continue


            
        
            