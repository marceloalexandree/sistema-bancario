saldo = 0
qtd_saques = 0
saque_maximo = 500
extrato = [f'Saldo Total: R${saldo:.2f}']
operacoes = 0
i = 0

while operacoes != 4:
    operacoes = int(input('Digite qual a operação desejada:\n[1] Depósito\n[2] Saque\n[3] Extrato \n[4] Sair\n'))
    
    if operacoes == 1:
        deposito = float(input('Digite o valor a ser depositado: R$ '))
        while deposito <= 0:
            print('Digite um valor válido para depósito!')
            deposito = float(input('Digite o valor a ser depositado: R$ '))
            
        if deposito > 0:
            saldo += deposito
            print(f'Novo saldo: R${saldo:.2f}')
            extrato.append(f'Depósito de R${deposito:.2f}')
            extrato[0] = f'Saldo Total: R${saldo:.2f}'
    elif operacoes == 2:
        if qtd_saques < 3:
            saque_desejado = float(input('Digite o valor a ser sacado: R$ '))
            while saque_desejado <= 0 or saque_desejado > saldo or saque_desejado > saque_maximo:
                print(f'Digite um valor válido para saque!\nSeu saldo atual é de R${saldo:.2f}')
                saque_desejado = float(input('Digite o valor a ser sacado: R$ '))
            if saque_desejado > 0 and saque_desejado <= saldo and saque_desejado <= saque_maximo:
                print(f'Saque de R${saque_desejado:.2f} efetuado com sucesso!')
                saldo -= saque_desejado
                extrato.append(f'Saque de R${saque_desejado:.2f}')
                qtd_saques += 1
                extrato[0] = f'Saldo Total: R${saldo:.2f}'
        else:
            print('Limite de 3 saques diários atingidos!')
    elif operacoes == 3:
        if len(extrato) > 1:
            x = len(extrato)
            i = x
            while x > 0:
                print(extrato[(i-x)])
                x -= 1
        else:
            print('Extrato vazio!\n')
    elif operacoes not in [1, 2, 3, 4]:
        print('Digite uma opção válida!')

print('Obrigado por usar o sistema bancário, até a próxima!')
