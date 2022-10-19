import pytest
from Projeto import *

class TestPublicJustificarTextos:

    def test_1(self):
        assert 'Fundamentos da Programacao' == limpa_texto('  Fundamentos\n\tda      Programacao\n')
    
    def test_2(self):
        assert ('Fundamentos da', 'Programacao') == corta_texto('Fundamentos da Programacao', 15)

    def test_3(self):
        assert 'Fundamentos  da Programacao!!!' == insere_espacos('Fundamentos da Programacao!!!', 30)

    def test_4(self):
        assert 'Fundamentos       da      Programacao!!!' == insere_espacos('Fundamentos da Programacao!!!', 40)

    def test_5(self):

        cad = ('Computers are incredibly  \n\tfast,     \n\t\taccurate'
            ' \n\t\t\tand  stupid.   \n    Human beings are incredibly  slow  '
            'inaccurate, and brilliant. \n     Together  they  are powerful   ' 
            'beyond imagination.')

        ref = ('Computers  are  incredibly  fast, accurate and stupid. Human',
            'beings   are  incredibly  slow  inaccurate,  and  brilliant.',
            'Together they are powerful beyond imagination.              ')
        assert ref == justifica_texto(cad, 60)
    


class TestPublicMetodoHondt:

    def test_1(self):

        ref =  {'A': [12000.0, 6000.0, 4000.0, 3000.0, 2400.0, 2000.0, 12000/7],
                    'B': [7500.0, 3750.0, 2500.0, 1875.0, 1500.0, 1250.0, 7500/7],
                    'C': [5250.0, 2625.0, 1750.0, 1312.5, 1050.0, 875.0, 750.0],
                    'D': [3000.0, 1500.0, 1000.0, 750.0, 600.0, 500.0, 3000/7]}

        hyp = calcula_quocientes({'A': 12000, 'B': 7500, 'C': 5250, 'D': 3000}, 7)
        
        assert ref == hyp
    
    def test_2(self):
        ref = ['A', 'B', 'A', 'C', 'A', 'B', 'D']
        assert ref == atribui_mandatos({'A': 12000, 'B': 7500, 'C': 5250, 'D': 3000}, 7)
    
    def test_3(self):
        info = {
            'Endor':   {'deputados': 7, 
                        'votos': {'A':12000, 'B':7500, 'C':5250, 'D':3000}},
            'Hoth':    {'deputados': 6, 
                        'votos': {'A':9000, 'B':11500, 'D':1500, 'E':5000}},
            'Tatooine': {'deputados': 3, 
                        'votos': {'A':3000, 'B':1900}}}

        ref = ['A', 'B', 'C', 'D', 'E']
        
        assert ref == obtem_partidos(info)
    
    def test_4(self):
        info = {
            'Endor':   {'deputados': 7, 
                        'votos': {'A':12000, 'B':7500, 'C':5250, 'D':3000}},
            'Hoth':    {'deputados': 6, 
                        'votos': {'A':9000, 'B':11500, 'D':1500, 'E':5000}},
            'Tatooine': {'deputados': 3, 
                        'votos': {'A':3000, 'B':1900}}}
        ref = [('A', 7, 24000), ('B', 6, 20900), ('C', 1, 5250), ('E', 1, 5000), ('D', 1, 4500)]
        
        assert ref == obtem_resultado_eleicoes(info)
    
    # -------------- Testes Repositorio LEIC -------------------------------------------
    def test_calcula_quocientes1(self):

        ref = {'A': [12000.0, 6000.0, 4000.0, 3000.0, 2400.0, 2000.0, 12000/7],
               'B': [7500.0, 3750.0, 2500.0, 1875.0, 1500.0, 1250.0, 7500/7],
               'C': [5250.0, 2625.0, 1750.0, 1312.5, 1050.0, 875.0, 750.0],
               'D': [3000.0, 1500.0, 1000.0, 750.0, 600.0, 500.0, 3000/7]}

        hyp = calcula_quocientes(
            {'A': 12000, 'B': 7500, 'C': 5250, 'D': 3000}, 7)

        assert ref == hyp

    def test_atribui_mandatos1(self):
        ref = ['A', 'B', 'A', 'C', 'A', 'B', 'D']
        assert ref == atribui_mandatos(
            {'A': 12000, 'B': 7500, 'C': 5250, 'D': 3000}, 7)

    def test_atribui_mandatos2(self):
        ref = ['A', 'B', 'A', 'C', 'A', 'B', 'D']
        assert ref == atribui_mandatos(
            {'D': 3000, 'B': 7500, 'C': 5250, 'A': 12000}, 7)

    def test_obtem_partidos1(self):
        info = {
            'Endor':   {'deputados': 7,
                        'votos': {'A': 12000, 'B': 7500, 'C': 5250, 'D': 3000}},
            'Hoth':    {'deputados': 6,
                        'votos': {'A': 9000, 'B': 11500, 'D': 1500, 'E': 5000}},
            'Tatooine': {'deputados': 3,
                         'votos': {'A': 3000, 'B': 1900}}}

        ref = ['A', 'B', 'C', 'D', 'E']

        assert ref == obtem_partidos(info)

    def test_obtem_resultado_eleicoes1(self):
        info = {
            'Endor':   {'deputados': 7,
                        'votos': {'A': 12000, 'B': 7500, 'C': 5250, 'D': 3000}},
            'Hoth':    {'deputados': 6,
                        'votos': {'A': 9000, 'B': 11500, 'D': 1500, 'E': 5000}},
            'Tatooine': {'deputados': 3,
                         'votos': {'A': 3000, 'B': 1900}}}
        ref = [('A', 7, 24000), ('B', 6, 20900),
               ('C', 1, 5250), ('E', 1, 5000), ('D', 1, 4500)]

        assert ref == obtem_resultado_eleicoes(info)

    def test_obtem_resultado_eleicoes2(self):
        info = {
            'Endor':   {'deputados': 12,
                        'votos': {'A': 117542, 'B': 79123, 'C': 47887, 'D': 28991}},
            'Hoth':    {'deputados': 4,
                        'votos': {'B': 47800, 'A': 56000, 'E': 12877, 'D': 28000}}}
        ref = [('A', 7, 173542), ('B', 5, 126923),
               ('D', 2, 56991), ('C', 2, 47887), ('E', 0, 12877)]

        assert ref == obtem_resultado_eleicoes(info)

    def test_obtem_resultado_eleicoes3(self):
        ref = [('bb', 2, 175000), ('BB', 2, 120000), ('D', 1, 93000), ('C', 0, 45000)] 
        info = {'Tatooine': {'deputados': 5, 'votos': {'BB': 120000, 'bb': 175000, 'C': 45000, 'D': 93000}}}
        assert ref == obtem_resultado_eleicoes(info)

    def test_obtem_resultados_eleicoes4(self):
        ref = [('PS', 21, 482606), ('PSD', 13, 285522), ('IL', 4, 93341), ('CH', 4, 91889), ('PCP', 2, 59995), ('BE', 2, 55786), ('L', 1, 28834), ('PAN', 1, 23577), ('CDS', 0, 19524)] 
        info = {'Lisboa': {'deputados': 48, 'votos': {'PS': 482606, 'PSD': 285522, 'IL': 93341, 'CH': 91889, 'PCP': 59995, 'BE': 55786, 'L': 28834, 'PAN': 23577, 'CDS': 19524}}} 
        assert ref == obtem_resultado_eleicoes(info)

    def test_obtem_resultados_eleicoes5(self):
        ref = [('PS', 19, 418869), ('PSD', 14, 318343), ('IL', 2, 50359), ('BE', 2, 47118), ('CH', 2, 42998), ('PCP', 1, 32277), ('PAN', 0, 16707), ('CDS', 0, 14347), ('L', 0, 11433)] 
        info = {'Porto': {'deputados': 40, 'votos': {'PS': 418869, 'PSD': 318343, 'IL': 50359, 'BE': 47118, 'CH': 42998, 'PCP': 32277, 'PAN': 16707, 'CDS': 14347, 'L': 11433}}} 
        assert ref == obtem_resultado_eleicoes(info)

    def test_obtem_resultados_eleicoes6(self):
        ref = [('PS', 5, 89870), ('PSD', 3, 58630), ('CH', 1, 23813), ('PCP', 0, 11854), ('BE', 0, 10012)] 
        info = {'Santarem': {'deputados': 9, 'votos': {'PS': 89870, 'PSD': 58630, 'CH': 23813, 'PCP': 11854, 'BE': 10012}}} 
        assert ref == obtem_resultado_eleicoes(info)

    def test_obtem_resultados_eleicoes7(self):
        ref = [('PS', 45, 991345), ('PSD', 30, 662495), ('CH', 7, 158700), ('IL', 6, 143700), ('BE', 4, 112916), ('PCP', 3, 104126), ('PAN', 1, 40284), ('L', 1, 40267), ('CDS', 0, 33871)] 
        info = {'Lisboa': {'deputados': 48, 'votos': {'PS': 482606, 'PSD': 285522, 'IL': 93341, 'CH': 91889, 'PCP': 59995, 'BE': 55786, 'L': 28834, 'PAN': 23577, 'CDS': 19524}}, 'Santarem': {'deputados': 9, 'votos': {'PS': 89870, 'PSD': 58630, 'CH': 23813, 'PCP': 11854, 'BE': 10012}}, 'Porto': {'deputados': 40, 'votos': {'PS': 418869, 'PSD': 318343, 'IL': 50359, 'BE': 47118, 'CH': 42998, 'PCP': 32277, 'PAN': 16707, 'CDS': 14347, 'L': 11433}}} 
        assert ref == obtem_resultado_eleicoes(info)


class TestPublicSistemasLineares:

    def test_1(self):
        assert produto_interno((1,2,3,4,5),(-4,5,-6,7,-8)) == -24.0

    
    def test_2(self):
        assert verifica_convergencia(((1, -0.5), (-1, 2)), (-0.4, 1.9), (0.1001, 1), 0.00001) == False

    def test_3(self):
        assert verifica_convergencia(((1, -0.5), (-1, 2)), (-0.4, 1.9), (0.1001, 1), 0.001) == True

    
    def test_4(self):
        assert retira_zeros_diagonal(((0, 1, 1), (1, 0, 0), (0, 1, 0)), (1, 2, 3)) == (((1, 0, 0), (0, 1, 0), (0, 1, 1)), (2, 3, 1))
    
    def test_5(self):
        assert eh_diagonal_dominante(((1, 2, 3, 4, 5),(4, -5, 6, -7, 8), (1, 3, 5, 3, 1), (-1, 0, -1, 0, -1), (0, 2, 4, 6, 8))) == False

    def test_6(self):
        assert eh_diagonal_dominante(((1, 0, 0), (0, 1, 0), (0, 1, 1))) == True
    '''
    def test_7(self):    
        def equal(x,y):
            delta = 1e-10
            return all(abs(x[i]-y[i])<delta for i in range(len(x)))

        A4, c4 = ((2, -1, -1), (2, -9, 7), (-2, 5, -9)), (-8, 8, -6)
        ref = (-4.0, -1.0, 1.0)
            
        assert equal(resolve_sistema(A4, c4, 1e-20), ref)
'''
        