import random

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
    'ganha_ia': 0,
    'ganha_xogador':0,
    'empate':0
    }

def colle_accion_xogador(Xogadas):
    # Pendiente de por try e capturar excepción!!!
    # O for tamen se pode por nunha lambda!!
    print('Escolla unha opción: ')
    for i in range(len(Xogadas)):
        print(i + 1, '. ', Xogadas[i])
    xogada = int(input())
    return Xogadas[xogada - 1]

def quen_ganha(accion_ia, accion_xogador,Regras):
    # Se as accions son iguais empate!
    if accion_ia == accion_xogador:
        print(f'Os dous escollestes {accion_ia}. Empate!')
        resultado = 'empate'
    # Ganha IA 
    elif accion_xogador in Regras[accion_ia]:
        print(f'{accion_ia} {Regras[accion_ia][accion_xogador]} {accion_xogador}. Perdeu...')
        resultado = 'ia'
    else:
        print(f'{accion_xogador} {Regras[accion_xogador][accion_ia]} {accion_ia}. Ganhou!!!')
        resultado = 'xogador'
    return resultado
   
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
    for i in Xogadas:
        lista_pesos.append(1)

    # Escollemos ao azar unha opcion 
    accion_ia_list = random.choices(Xogadas, weights=lista_pesos,k=1)
    accion_ia = accion_ia_list[0]

    accion_xogador = colle_accion_xogador(Xogadas)

    print(quen_ganha(accion_ia,accion_xogador,Regras))

if __name__ == "__main__":
    main()
