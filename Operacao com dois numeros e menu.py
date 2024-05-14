n3=''
while n3!=5:
    try:
        n1=float(input('Digite um número:'))
        n2=float(input('Digite outro: '))
    except ValueError:
        print('Digite apenas valores numéricos.')
        continue
    soma=n1+n2
    mult=n1*n2
    menu=print('''Agora, nos diga qual operação você quer realizar de acordo com o menu abaixo:
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR 
    [ 3 ] MAIOR 
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    try:
        n3=float(input('Digite a operação: '))
    except ValueError:
        print('Digite apenas valores numéricos.')
        continue
    if n3==1:
        print('A soma entre os números é: {}'.format(soma))
    elif n3==2:
        print('A multiplicação entre os números é: {}'.format(mult))
    elif n3==3:
        if n1>n2:
            print('O maior valor entre esses números é: {}'.format(n1))
        if n2>n1:
            print('O maior valor entre esses números é: {}'.format(n2))
        if n1==n2:
            print('Não há valor maior. Os números são iguais.')
    elif n3==4:
        continue
    elif n3!=1 and n3!=2 and n3!=3 and n3!=4 and n3!=5:
        print('Digite uma operação válida!')
print('---------- PROGRAMA ENCERRADO ----------')