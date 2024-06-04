while True:
    ced50=ced20=ced10=ced1=0
    print('='*35)
    print(f'{'ATM BANK':^35}')
    print('='*35)
    n1=int(input('Quantos reais você quer sacar? R$'))
    print('='*35)
    if n1==0:
        break
    while n1>=50:
        n1-=50
        ced50+=1
    while n1>=20 and n1<50:
        n1-=20
        ced20+=1
    while n1>=10 and n1<20:
        n1-=10
        ced10+=1
    while n1>=1 and n1<10:
        n1-=1
        ced1+=1
    if ced50>0:
        print(f'Total de {ced50} cédulas de R$50')
    if ced20>0:
        print(f'Total de {ced20} cédulas de R$20')
    if ced10>0:
        print(f'Total de {ced10} cédulas de R$10')
    if ced1>0:
        print(f'Total de {ced1} cédulas de R$1')
print(f'{'Fim':^35}')
print('='*35)