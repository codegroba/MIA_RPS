# Diccionario que garda as posibles xogadas e a quen gaña
Regras = {
    'pedra':['tesoira'],
    'papel':['pedra'],
    'tesoira':['papel'],
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
    print('Escolla unha opción: ')
    for i in range(len(Xogadas)):
        print(i + 1, '. ', Xogadas[i])
    xogada = int(input())
    return Xogadas[xogada - 1]



def main():
    # Collemos as xogadas e almacenamolas nunha lista
    Xogadas = list(Regras.keys())

    accion_xogador = colle_accion_xogador(Xogadas)
    print('Escolleu ', accion_xogador)


if __name__ == "__main__":
    main()
