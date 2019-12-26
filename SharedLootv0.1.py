titulo = 'Shared Loot v0.10 by FábioJ.R'
print ('=-='*15)
print (f'{titulo:-^45}')
print ('=-='*15)
print ('\n')
team = int (input('Qual o tamanho do time?'))

###LISTA####
knight = ['nome', 'balance']
druid = ['nome', 'balance']
paladin = ['nome', 'balance']
sorcerer = ['nome', 'balance']

#totalx2 = knight[1]+druid[1]
#totalx3 = knight[1]+druid[1]+paladin[1]
#totalx4 = knight[1]+druid[1]+paladin[1]+sorcerer[1]
#####CONDIÇÃO#####

    
if team == 2:
    knight[0] = str (input('Qual o nome do Ek?'))
    knight[1] = float (input('Qual o balance do Ek?:'))
    druid[0] = str (input('Qual o nome do Ed?:'))
    druid[1] = float (input('Qual o balance do druid?:'))
    totalx2 = knight[1]+druid[1]
    lucro = totalx2/2
    print (f'O balance total foi de {knight[1]+druid[1]:.3f}k.')
    print (f'O balance de {knight[0]} foi: {knight[1]:.3f}k,  e de {druid[0]} foi: {druid[1]:.3f}k.')
    if totalx2 > 0:    
        print (f'O Lucro para cada foi de {lucro:.3f}k.')
        #print (f' O {knight[0]} deve pagar {lucro}+{druid[1]}={lucro} ao {druid[0]}.')
        if knight[1]>0:
            print (f' O {knight[0]} deve pagar {lucro-druid[1]:.3f}k ao {druid[0]}.')
        elif druid[1]>knight[1]:
            print (f' O {druid[0]} deve pagar {lucro-knight[1]:.3f}k ao {knight[0]}')
    else:
        print (f'O Waste pra cada foi de {totalx2/2}k.') 
if team ==3:
    knight[0] = str (input('Qual o nome do Ek?:'))
    knight[1] = float (input('Qual o balance do Ek?:'))
    druid[0] = str (input('Qual o nome do Ed?:'))
    druid[1] = float (input('Qual o balance do druid?:'))
    paladin[0] = str (input('Qual o nome do Ms ou Rp?:'))
    paladin[1] = float (input('Qual o balance do Ms ou Rp?:'))
if team ==4:
    knight[0] = str (input('Qual o nome do Ek?:'))
    knight[1] = float (input('Qual o balance do Ek?:'))
    druid[0] = str (input('Qual o nome do Ed?:'))
    druid[1] = float (input('Qual o balance do druid?:'))
    paladin[0] = str (input('Qual o nome do Ms ou Rp?:'))
    paladin[1] = float (input('Qual o balance do Ms ou Rp?:'))
    sorcerer[0] = str (input('Qual o nome do Ms ou Rp?:'))
    sorcerer[1] = float (input('Qual o balance do Ms ou Rp?:'))




