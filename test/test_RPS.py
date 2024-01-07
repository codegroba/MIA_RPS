import pytest 
from src.RPS import quen_ganha

# Diccionario que garda as posibles xogadas e a quen gaña
RegrasRPS = {
        'pedra':{'tesoira':'esmaga'},
        'papel':{'pedra':'envolve'},
        'tesoira':{'papel':'corta'},
    }

def test_empates():
    xogadas = list(RegrasRPS.keys())
    for i in xogadas:
        assert 'empate' == quen_ganha(i,i,RegrasRPS)

def test_ganha_ia():
    xogadas = list(RegrasRPS.keys())
    for i in xogadas:
        for j in RegrasRPS[i]:
            assert 'ia' == quen_ganha(i,j,RegrasRPS)

def test_ganha_xogador():
    xogadas = list(RegrasRPS.keys())
    for i in xogadas:
        aux_xogadas = list(RegrasRPS.keys())
        for j in RegrasRPS[i]:
            aux_xogadas.remove(j)
        for k in aux_xogadas:
            if i != k:
                assert 'xogador' == quen_ganha(i,k,RegrasRPS)
