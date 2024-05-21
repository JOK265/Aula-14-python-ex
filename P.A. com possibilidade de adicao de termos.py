try:
    n1=int(input('Digite o primeiro termo: '))
    n2=int(input('Digite a razão: '))
except ValueError:
    print('Digite apenas números inteiros!')
n3=1
while n3!=11:                       # No fim desse laço while o n3 vai ser igual a 11 
    pa=n1+(n3-1)*n2
    n3+=1
    print(pa)
n4=1
while n4!=0:
    try:
        n4=int(input('Quantos mais termos quer ver dessa P.A.? '))            # Aqui n4 recebe o valor do input. Sendo n4=0, o programa é encerrado
    except ValueError:
        print('Digite apenas números inteiros!')
        continue
    if n4>0:                                # Sendo n4>0, o programa soma o valor do input de n4 mais n3
        n4+=n3                # n4 passa a ter o valor de n4+n3
        while n3!=n4:                         # enquanto n3 permanece com o valor do fim do primeiro laço(de 11), fazemos a PA baseada no valor de n3 e somamos 1 a este até que se iguale ao valor de n4+n3
            pa=n1+(n3-1)*n2
            n3+=1
            print(pa)
    else:
        print('========PROGRAMA ENCERRADO!========')