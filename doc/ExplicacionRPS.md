## Explicación código RPS

Al inicio del programa importaremos as librerías. 

```python
import random
from statistics import multimode
```

Para o programa empregaremos a librería random, que nos vai permitir escoller de maneira aleatoria unha opción dunha lista e tamen statictics, esta última precisaremola para calcular unha media aritmética.

O programa parte dun deseño no cal as regras introducense mediante un diccionario Python. Deste xeito o código será o mesmo para RPS ou RPSLS. Ao inicio daranos a escoller se queremos xogar a un ou outro.

```Python
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
```

Para o almacenamento de datos empregaremos diccionarios e listas.

```Python
# Almacenamento de datos
hist_xogador = []
hist_ia = []
hist_resultados = {
    'ia': 0,
    'xogador':0,
    'empate':0
    }
```

Comezaremos vendo a main e despois iremos coas funcións. O primeiro que faremos tal como comentamos anteriormente é escoller o xogo. Según o que escollamos cargarase un ou outro diccionario de regras.

```Python
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
```

Agora é o momento de inicializar variables que empregaremos durante o xogo. Estas van depender das regras, básicamente xeraremos unha lista de 'pesos' a cal profundizaremos mais adiante.

```Python
    # Collemos as xogadas e almacenamolas nunha lista
    Xogadas = list(Regras.keys())
    # Criamos unha lista na que imos a darlle os pesos de probabilidade
    # Criaremolo con tandos elementos como xogadas posibles
    lista_pesos = []
    pesos = {}
    for i in Xogadas:
        pesos[i] = 1
        lista_pesos.append(1)
```

A idea do programa é almacenar os historiais de xogadas, tanto da IA como do xogador e mais o resultado das partidas. As xogadas da IA vanse escoller dunha lista aleatoriamente. A fución random permítenos engadirlle unha lista coas opcións e outra segunda co peso de cada opción. Os pesos van infuír na probabilidade de escoller as opcións, enton segundo os pesos que lle asignemos imos ter mais probabilidade de que xogue unha cousa ou outra.

Voltamos ao código! Neste punto entraremos nun buble que é no que vai a estar durante todas as xogadas que queiramos na partida. Actualizamos a lista de pesos (no inicio todos os pesos son iguais co cal sacaremos unha xogada random).

```Python
while True:
        # Actualizamos a lista de pesos
        lista_pesos = list(pesos.values())
        # Escollemos ao azar unha opcion 
        accion_ia_list = random.choices(Xogadas, weights=lista_pesos,k=1)
        accion_ia = accion_ia_list[0]
```

Chamamos a funcion na que lle diremos ao xogador que escolla unha xogada.

```Python
 # Pedimoslle ao xogador que escolla unha opcion
 accion_xogador = colle_accion_xogador(Xogadas)
```

Recollemos datos, imprimimos quen gañou e o historial da partida.

```Python
# Gardamos datos
hist_ia.append(accion_ia)
hist_xogador.append(accion_xogador)
resultado = quen_ganha(accion_ia,accion_xogador,Regras)
hist_resultados[resultado] = hist_resultados[resultado] + 1
print('\nResultados: \nMáquina: ',hist_resultados['ia'],'\nXogador: ',hist_resultados['xogador'],'\nEmpates: ',hist_resultados['empate'])
```

Agora unha vez temos datos imos a xogar cos pesos chamando as funcións que os modifican. Iremos coas funcións mais adiante. Polo momento contamos con dúas, pero podense engadir as que queiramos.

```Python
# Reset pesos 
for i in Xogadas:
    pesos[i] = 1
# Calculamos os pesos
pesos = mais_comun(hist_xogador, Regras, pesos)
pesos = menos_comun(hist_xogador, Regras, pesos)
```

Pediremos que queremos seguir xogando ou saír.

```Python
if not outra_ronda():
     break
```

### Función 'colle_acción_xogador'

Imprime entre que xogadas podemos escoller e captura a introducida polo usuario.

```Python
def colle_accion_xogador(Xogadas):
    print('Escolla unha opción: ')
    for i in range(len(Xogadas)):
        print(i + 1, '. ', Xogadas[i])
    xogada = int(input())
    return Xogadas[xogada - 1]
```

### Función 'quen_ganha'

Entregamoslle que xogou cada un dos contrincantes mais as regras e diranos quen gañou ou se empataron.

```Python
def quen_ganha(accion_ia, accion_xogador,Regras):
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
```

### Función 'mais_comun'

Esta é unha das funcións que van a modificar os pesos na probabilidade de escoller unha xogada. A premisa é que se o noso rival escolle mais veces unha xogada nos aumentemos a probabilidade da escoller as que gañan ao que el mais saque.

```Python
def mais_comun(hist_xogador, Regras, pesos):
    mais_repetidos = multimode(hist_xogador)
    for i in mais_repetidos:
        for j in quen_ganha_a(i, Regras):
            pesos[j] = pesos[j] + 5
    return pesos
```

### Función 'quen_ganha_a'

Empregaa a función anteriormente citada. Se lle entregamos unha xogada diranos que xogada ou xogadas lle gañan a que lle entregamos.

```Python
def quen_ganha_a(xogada, Regras):
    Xogadas = list(Regras.keys())
    lista_quen_ganha = []
    for i in Xogadas:
        if xogada in Regras[i]:
            lista_quen_ganha.append(i)
    return lista_quen_ganha
```

### Función 'menos_común'

Esta é a segunda das funcións que modifican os pesos. Se vemos que o xogador saca menos unha xogada que o resto, daremoslle máis probabilidade de sacar as xogadas que perdan co que menos saque.

```Python
def menos_comun(hist_xogador, Regras, pesos):
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
```

### Función 'outra_ronda'

Escolleremos entre saír ou continuar.

```Python
def outra_ronda():
    outra = input('\nOutra ronda? (s/n): ')
    return outra.lower() == 's'
```