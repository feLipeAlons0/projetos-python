def calculo_energia():

    def reciclo():
        reciclo_ = int(input(
            'Deseja refazer o calculo?\n1. Sim\n2. Não\n--> '))

        match (reciclo_):
            case 1:
                calculo_energia()
            case 2:
                print('Obrigado.')
            case _:
                print('O valor deve estar listado na opções.')
                reciclo()

    def confirmacao(tipo_de_instalacao):
        match (tipo_de_instalacao):
            case 1 | 2 | 3:
                instalacao = input(f'Você digitou o número {
                                   tipo_de_instalacao}, está correto?\n1. Sim\n2. Não\n-->')
                if (instalacao == '1'):
                    tipo_de_instalacao = tipo_de_instalacao
                else:
                    reciclo()
            case _:
                print('O número deve estar entre as opções!')
                reciclo()

    print('Olá, seja bem vindo ao nosso atendimento,'
          'vamos calcular o seu consumo de energia elétrica')
    try:
        quantidade_consumida = float(
            input('Digite a quantidade de KWh que foi consumida: '))
        tipo_de_instalacao = int(input(
            'Qual o tipo da sua instalação:\n1. Residencial\n2. Comercial\n3. Industrial\n--> '))
        confirmacao(tipo_de_instalacao)

    except:
        print('Ops, verificamos aqui que você não digitou um valor correto, na quantidade consumida de KWh, deve conter apenas números.')
        calculo_energia()
#comentario teste
    match (tipo_de_instalacao):
        case 1:
            if (quantidade_consumida <= 500):
                A = 0.40
                B = quantidade_consumida * A
                print(f'O valor da sua conta é de {B:.2f}R$')
                reciclo()
            elif (quantidade_consumida > 500):
                C = 0.65
                D = quantidade_consumida * C
                print(f'O valor da sua conta é de {D:.2f}R$')
                reciclo()
        case 2:
            if (quantidade_consumida <= 1000):
                E = 0.55
                F = quantidade_consumida * E
                print(f'O valor da sua conta é de {F:.2f}R$')
                reciclo()
            elif (quantidade_consumida > 1000):
                G = 0.60
                H = quantidade_consumida * G
                print(f'O valor da sua conta é de {H:.2f}R$')
                reciclo()
        case 3:
            if (quantidade_consumida <= 5000):
                I = 0.55
                J = quantidade_consumida * I
                print(f'O valor da sua conta é de {J:.2f}R$')
                reciclo()
            elif (quantidade_consumida > 5000):
                K = 0.60
                L = quantidade_consumida * K
                print(f'O valor da sua conta é de {L:.2f}R$')
                reciclo()
        case _:
            print('O valor deve estar entre uma das opções')
            reciclo()


calculo_energia()
