titulo = 'Shared Loot v0.10 by FábioJ.R'
print ('=-='*15)
print (f'{titulo:-^45}')
print ('=-='*15)
print ('\n')
team = int (input('Quantos Players tem no Time? Responda "2" para x2, "3" para x3 e "4" para x4.   '))

###LISTA####
knight = ['nome', 'balance']
druid = ['nome', 'balance']
paladin = ['nome', 'balance']
sorcerer = ['nome', 'balance']

###ORDEM DE BALANCE###
a = knight
b = druid
c = paladin
d = sorcerer
# por padrão o knight será o maior balance
#if druid[1] > knight[1] and druid[1] > paladin[1] and druid[1] > sorcerer[1]: #Druid maior balance
  #  a = druid
    #b = knight
#if paladin[1] > knight[1] and paladin[1] > druid[1] and paladin[1] > sorcerer[1]: #paladin maior balance
    #a = paladin
    #c = knight
#if sorcerer[1] > knight[1] and sorcerer[1] > druid[1] and sorcerer[1] > paladin[1]: #sorcerer maior balance
    #a = sorcerer
    #d = knight


if team == 2:
    knight[0] = str(input('Qual nome do EK?   '))
    knight[1] = float (input('Qual o balance do EK?   '))
    druid[0] = str(input('Qual nome do ED?   '))
    druid[1] = float (input('Qual balance do ED?   '))
    if druid[1] > knight[1]:
        a = druid
        b = knight
    print(f'O balance do {a[0]} foi: {a[1]:.3f}k, e o de {b[0]} foi: {b[1]:.3f}k')
    total = a[1] + b[1] #or druid[1] + knight[1]
    lucro = total / 2
    print (f'O balance total foi de {total:.3f}k, e o lucro para cada foi de {lucro:.3f}')
    print(f'O {a[0]}, deve pagar {lucro-b[1]:.3f}k para o {b[0]}.')

if team == 3:
    knight[0] = str(input('Qual nome do Ek?   '))
    knight[1] = float(input('Qual balance do Ek?   '))
    druid[0] = str(input('Qual nome do Ed?   '))
    druid[1] = float(input('Qual balance do Ed?   '))
    paladin[0] = str(input('Qual nome do Rp ou Ms?   '))
    paladin[1] = float(input('Qual balance do Rp ou Ms?   '))

    totalx3 = a[1] + b[1] + c[1] #Somatório dos balances!

    lucro = totalx3 / 3 #Divisão pela quantidade de players

    if paladin[1] > knight[1] and paladin[1] > druid[1] and knight[1] > druid[1]: #paladin maior balance / com Ek maior balance que Ed
        a = paladin
        b = knight
        c = druid
    elif paladin[1] > knight[1] and paladin[1] > druid[1] and druid[1] > knight[1]:#paladin maior balance / com Ek menor balance que Ed
        a = paladin
        b = druid
        c = knight   
    if druid[1] > knight[1] and druid[1] > paladin[1] and knight[1] > paladin[1]: #druid maior balance / com Ek maior balance que RP
        a = druid
        b = knight
        c = paladin
    elif druid[1] > knight[1] and druid[1] > paladin[1] and paladin[1] > knight[1]:#druid maior balance / com Ek menor balance que RP
        a = druid
        b = paladin
        c = knight

    lucroA = lucro-a[1]
    lucroB = lucro-b[1]
    lucroC = lucro-c[1]

    #print (f'Lucro do {a[0]} é: {lucroA:.3f}k') #Testando resultado
    #print (f'Lucro do {b[0]} é: {lucroB:.3f}k') #Testando Resultado
    #print (f'Lucro do {c[0]} é: {lucroC:.3f}k') #Testando Resultado

    if a[1] > lucro: # Lucro da Posição 1 / Maior Balance da pt
        print(f'O Balance de {a[0]}, foi: {a[1]:.3f}k') 
        print(f'deve pagar {lucroB:.3f}k para {b[0]} ') 
        print(f'deve pagar {lucroC:.3f}k para {c[0]} ')
    #print(f'O Balance de {a[0]}, foi: {a[1]:.3f}k. O {a[0]}, deve pagar {lucro-b[1]:.3f} para {b[0]}.')

    if b[1] > 0 and b[1] > lucro: #LUCRO DA POSIÇÃO 2 
        print(f'O Balance de {b[0]}, foi: {b[1]:.3f}k, deve pagar {b[1]-lucro:.3f}k para {a[0]}')
    else:
        print (f'O balance de {b[0]}, foi: {b[1]:.3f}k')
        

    if c[1] > 0 and c[1] > lucro: #Lucro da posição 3
        print(f'O Balance de {c[0]}, foi: {c[1]:.3f}k, deve pagar {lucroC:.3f}k para {a[0]}')
    else:
        print (f'O balance de {c[0]}, foi: {c[1]:.3f}k.')
        

    

    print(f'O Balance total foi: {totalx3:.3f}k, e o lucro pra cada foi: {lucro:.3f}')



if team == 4:
    knight[0] = str(input('Qual nome do Ek?   '))
    knight[1] = float(input('Qual balance do Ek?   '))
    druid[0] = str(input('Qual nome do Ed?   '))
    druid[1] = float(input('Qual balance do Ed?   '))
    paladin[0] = str(input('Qual nome do Rp ou Ms?   '))
    paladin[1] = float(input('Qual balance do Rp?   '))
    sorcerer[0] = str(input('Qual nome do Ms?   '))
    sorcerer[1] = float(input('Qual o balance do Ms?'))

    totalx4 = a[1] + b[1] + c[1] + d[1] #Somatório dos balances!

    lucro = totalx4 / 4 #Divisão pela quantidade de players

    if paladin[1] > knight[1] and paladin[1] > druid[1] and paladin[1] > sorcerer[1] and knight[1] > druid[1] and knight[1] > sorcerer[1] and druid[1] > sorcerer[1] : 
        #paladin maior balance / com Ek maior balance que Ed / e ed maior balance que ms
        a = paladin
        b = knight
        c = druid
        d = sorcerer
    elif paladin[1] > knight[1] and paladin[1] > druid[1] and paladin[1] > sorcerer[1] and knight[1] > druid[1] and knight[1] > sorcerer[1] and druid[1] < sorcerer[1] : 
        #paladin maior balance / com Ek maior balance que Ed e ms / e ed maior balance que ms
        a = paladin
        b = knight
        c = sorcerer  
        d = druid
    elif paladin[1] > knight[1] and paladin[1] > druid[1] and paladin[1] > sorcerer[1] and knight[1] < druid[1] and knight[1] > sorcerer[1] and druid[1] > sorcerer[1] : 
        #paladin maior balance / com Ek maior balance que ms e menor que ed 
        a = paladin
        b = druid
        c = knight  
        d = sorcerer
    elif paladin[1] > knight[1] and paladin[1] > druid[1] and paladin[1] > sorcerer[1] and knight[1] < druid[1] and knight[1] > sorcerer[1] and druid[1] > sorcerer[1] : 
        #paladin maior balance / com Ek maior balance que Ed e menor que Ms 
        a = paladin
        b = sorcerer
        c = knight  
        d = druid
     elif paladin[1] > knight[1] and paladin[1] > druid[1] and paladin[1] > sorcerer[1] and knight[1] < druid[1] and knight[1] > sorcerer[1] and druid[1] > sorcerer[1] : 
        #paladin maior balance / com Ek maior balance que ms e menor que ed / e ed maior balance que ms
        a = paladin
        b = druid
        c = knight  
        d = sorcerer
    if druid[1] > knight[1] and druid[1] > paladin[1] and knight[1] > paladin[1]: 
        #druid maior balance / com Ek maior balance que RP
        a = druid
        b = knight
        c = paladin
    elif druid[1] > knight[1] and druid[1] > paladin[1] and paladin[1] > knight[1]:
        #druid maior balance / com Ek menor balance que RP
        a = druid
        b = paladin
        c = knight

    lucroA = lucro-a[1]
    lucroB = lucro-b[1]
    lucroC = lucro-c[1]

    #print (f'Lucro do {a[0]} é: {lucroA:.3f}k') #Testando resultado
    #print (f'Lucro do {b[0]} é: {lucroB:.3f}k') #Testando Resultado
    #print (f'Lucro do {c[0]} é: {lucroC:.3f}k') #Testando Resultado

    if a[1] > lucro: # Lucro da Posição 1 / Maior Balance da pt
        print(f'O Balance de {a[0]}, foi: {a[1]:.3f}k') 
        print(f'deve pagar {lucroB:.3f}k para {b[0]} ') 
        print(f'deve pagar {lucroC:.3f}k para {c[0]} ')
    #print(f'O Balance de {a[0]}, foi: {a[1]:.3f}k. O {a[0]}, deve pagar {lucro-b[1]:.3f} para {b[0]}.')

    if b[1] > 0 and b[1] > lucro: #LUCRO DA POSIÇÃO 2 
        print(f'O Balance de {b[0]}, foi: {b[1]:.3f}k, deve pagar {b[1]-lucro:.3f}k para {a[0]}')
    else:
        print (f'O balance de {b[0]}, foi: {b[1]:.3f}k')
        

    if c[1] > 0 and c[1] > lucro: #Lucro da posição 3
        print(f'O Balance de {c[0]}, foi: {c[1]:.3f}k, deve pagar {lucroC:.3f}k para {a[0]}')
    else:
        print (f'O balance de {c[0]}, foi: {c[1]:.3f}k.')
        

    

    print(f'O Balance total foi: {totalx3:.3f}k, e o lucro pra cada foi: {lucro:.3f}')



