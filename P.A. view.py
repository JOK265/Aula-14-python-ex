n1=None
n2=None
while n1 is None or n2 is None:
    try:
        n1=int(input('Digite o primeiro termo: '))
        n2=int(input('Digite a razão: '))
    except ValueError:
        print('Digite apenas valores numéricos!')
        n1=None
        n2=None
n3=1
while n3!=11:
    pa=n1+(n3-1)*n2
    print(f'{n3}º termo: {pa}')
    n3+=1
n4='s'
while n4=='s':
    n4=input('Quer ver mais termos dessa P.A.? [S/N] ').strip().lower()
    if n4=='s':
        n5=int(input('Quantos mais termos você quer ver dessa P.A.? '))
        if n5>0:
            n5+=n3
            while n3!=n5:
                pa=n1+(n3-1)*n2
                print(f'{n3}º termo: {pa}')
                n3+=1
        elif n5<0:
            n5+=n3
            while n3!=n5:
                n3-=1
                pa=n1+(n3-1)*n2
                print(f'{n3}º termo: {pa}')
    elif n4=='n':
        print('==========PROGRAMA ENCERRADO==========')
    elif n4!='s' and n4!='n':
        print('Digite uma opção válida!')
