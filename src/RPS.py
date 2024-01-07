import random
from statistics import multimode

# Diccionario que garda as posibles xogadas e a quen gaña
RegrasRPS = {
        'pedra':{'tesoira':'esmaga'},
        'papel':{'pedra':'envolve'},
        'tesoira':{'papel':'corta'},
    }

RegrasRPSLS = {
        'pedra':{
            'lagarto':'esmaga',
            'tesoira':'esmaga'
        },
        'papel':{
            'pedra':'envolve',
            'spock':'desautoriza'
        },
        'tesoira':{
            'papel':'corta',
            'lagarto':'decapita'
        },
        'lagarto':{
            'spock':'envenena',
            'papel':'come'
        },
        'spock':{
            'tesoira':'rompe',
            'pedra':'vaporiza'
        }
    }

# Almacenamento de datos
hist_xogador = []
hist_ia = []
hist_resultados = {
    'ia': 0,
    'xogador':0,
    'empate':0
    }

def colle_accion_xogador(Xogadas):
    '''
    Imprime mensaxe coas opcions e captura en entregada polo usuario
    '''
    # Pendiente de por try e capturar excepción!!!
    # O for tamen se pode por nunha lambda!!
    print('Escolla unha opción: ')
    for i in range(len(Xogadas)):
        print(i + 1, '. ', Xogadas[i])
    xogada = int(input())
    return Xogadas[xogada - 1]

def quen_ganha(accion_ia, accion_xogador,Regras):
    '''
    Entregamoslle as accions da ia e do xogador e dinos
    se empataron ou quen deles ganhou.
    '''
    # Se as accions son iguais empate!
    if accion_ia == accion_xogador:
        print(f'Os dous escollestes {accion_ia}. Empate!')
        resultado = 'empate'
    # Ganha IA 
    elif accion_xogador in Regras[accion_ia]:
        print(f'{accion_ia} {Regras[accion_ia][accion_xogador]} {accion_xogador}. Perdeu...')
        resultado = 'ia'
    # Ganha xogador
    else:
        print(f'{accion_xogador} {Regras[accion_xogador][accion_ia]} {accion_ia}. Ganhou!!!')
        resultado = 'xogador'
    return resultado

def quen_ganha_a(xogada, Regras):
    '''
    Dandolle unha xogada dinos quen lle ganha a esa xogada
    '''
    Xogadas = list(Regras.keys())
    lista_quen_ganha = []
    for i in Xogadas:
        if xogada in Regras[i]:
            lista_quen_ganha.append(i)
    return lista_quen_ganha

def mais_comun(hist_xogador, Regras, pesos):
    '''
    Daremoslle mais probabilidade de sair aos que ganhen ao mais comun.
    '''
    mais_repetidos = multimode(hist_xogador)
    for i in mais_repetidos:
        for j in quen_ganha_a(i, Regras):
            pesos[j] = pesos[j] + 5
    return pesos

def menos_comun(hist_xogador, Regras, pesos):
    '''
    Daremoslle mais probabilidade de sair aos que perdan co menos comun.
    '''
    dic_xogadas = {}
    lista_menos_comun = []
    xogadas = list(Regras.keys())
    for i in xogadas:
        dic_xogadas[i] = 0

    for i in hist_xogador:
        dic_xogadas[i] = dic_xogadas[i] + 1
    # Buscamos o valor minimo
    key_val_min = min(dic_xogadas,key=dic_xogadas.get)
    val_min = dic_xogadas[key_val_min]
    # Percorremos o diccionario para ver se hai mais de un.
    for key, value in dic_xogadas.items():
        if val_min == value:
            lista_menos_comun.append(key)
    # Damoslle mais probabilidade de sair aos que perdan co menos comun 
    for i in lista_menos_comun:
        for j in Regras[i]:
            pesos[j] = pesos[j] + 5
    return pesos

def outra_ronda():
    '''
    Pregunta se queremos seguir xogando.
    '''
    outra = input('\nOutra ronda? (s/n): ')
    return outra.lower() == 's'

def main():
    # Escollemos xogo
    print(f'Escolla xogo: \n 1. RPS\n 2. RPSLS')
    xogo =int(input())
    if xogo == 1:
        Regras = RegrasRPS
    elif xogo == 2:
        Regras = RegrasRPSLS
    else:
        Regras = RegrasRPS

    # Collemos as xogadas e almacenamolas nunha lista
    Xogadas = list(Regras.keys())
    # Criamos unha lista na que imos a darlle os pesos de probabilidade
    # Criaremolo con tandos elementos como xogadas posibles
    lista_pesos = []
    pesos = {}
    for i in Xogadas:
        pesos[i] = 1
        lista_pesos.append(1)

    while True:
        # Actualizamos a lista de pesos
        lista_pesos = list(pesos.values())
        # Escollemos ao azar unha opcion 
        accion_ia_list = random.choices(Xogadas, weights=lista_pesos,k=1)
        accion_ia = accion_ia_list[0]
        
        # Pedimoslle ao xogador que escolla unha opcion
        accion_xogador = colle_accion_xogador(Xogadas)

        # Gardamos datos
        hist_ia.append(accion_ia)
        hist_xogador.append(accion_xogador)
        resultado = quen_ganha(accion_ia,accion_xogador,Regras)
        hist_resultados[resultado] = hist_resultados[resultado] + 1

        # print(f'\nhist ia: {hist_ia}')
        # print(f'\nhist xogaror: {hist_xogador}')
        print('\nResultados: \nMáquina: ',hist_resultados['ia'],'\nXogador: ',hist_resultados['xogador'],'\nEmpates: ',hist_resultados['empate'])

        # Reset pesos 
        for i in Xogadas:
            pesos[i] = 1
        # Calculamos os pesos
        pesos = mais_comun(hist_xogador, Regras, pesos)
        # print('peso1 ', pesos)
        pesos = menos_comun(hist_xogador, Regras, pesos)
        # print('peso2 ', pesos)

        if not outra_ronda():
            break

if __name__ == "__main__":
    main()
