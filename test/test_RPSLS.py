import pytest 
from src.RPS import quen_ganha

# Diccionario que garda as posibles xogadas e a quen gaña
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

def test_empates():
    xogadas = list(RegrasRPSLS.keys())
    for i in xogadas:
        assert 'empate' == quen_ganha(i,i,RegrasRPSLS)

def test_ganha_ia():
    xogadas = list(RegrasRPSLS.keys())
    for i in xogadas:
        for j in RegrasRPSLS[i]:
            assert 'ia' == quen_ganha(i,j,RegrasRPSLS)

def test_ganha_xogador():
    xogadas = list(RegrasRPSLS.keys())
    for i in xogadas:
        aux_xogadas = list(RegrasRPSLS.keys())
        for j in RegrasRPSLS[i]:
            aux_xogadas.remove(j)
        for k in aux_xogadas:
            if i != k:
                assert 'xogador' == quen_ganha(i,k,RegrasRPSLS)
