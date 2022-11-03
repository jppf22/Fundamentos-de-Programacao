import pytest
import sys
from Minesweeper import *

class TestPublicGerador:

    # b tem que ser 32 ou 64 inteiros
    def test_cria_gerador_arg1(self):
        with pytest.raises(ValueError,match="cria_gerador: argumentos invalidos"):
            cria_gerador(40,1)

    def test_cria_gerador_arg2(self):
        with pytest.raises(ValueError,match="cria_gerador: argumentos invalidos"):
            cria_gerador(32.0,1)
    
    #s tem que ser inteiro positivo
    def test_cria_gerador_arg3(self):
        with pytest.raises(ValueError,match="cria_gerador: argumentos invalidos"):
            cria_gerador(32,-1)
    
    def test_cria_gerador_arg4(self):
        with pytest.raises(ValueError,match="cria_gerador: argumentos invalidos"):
            cria_gerador(32,1.0)
    
    #a copia do gerador não pode ter a mesma adress do original
    def test_copia_gerador(self):
        g1 = cria_gerador(32,1)
        g2 = cria_copia_gerador(g1)
        assert(id(g2) != id(g1))

    def test_eh_gerador_tuple(self):
        assert(eh_gerador((32,1)) == False)
    
    def test_eh_gerador_float(self):
        assert(eh_gerador([32,1.0]) == False)
    
    def test_eh_gerador_invalidbits(self):
        assert(eh_gerador([30,1]) == False)
    
    def test_eh_gerador_inf0(self):
        assert(eh_gerador([32,0]) == False)
    
    def test_eh_gerador_vdd(self):
        assert(eh_gerador([32,1]) == True)
    
    def test_geradores_iguais_vdd(self):
        assert(geradores_iguais([32,1],[32,1]) == True)
    
    def test_geradores_iguais_tiposdiff(self):
        assert(geradores_iguais([32,1],(32,1)) == False)
    
    def test_geradores_iguais_seeddiff(self):
        assert(geradores_iguais([32,2],[32,1]) == False)
    
    def test_geradores_iguais_bitdiff(self):
        assert(geradores_iguais([32,1],[64,1]) == False)
    
    def test_gerador_para_str_vdd(self):
        assert(gerador_para_str([32,1]) == "xorshift32(s=1)")
    
    def test_geradpr_para_str_seedgrande(self):
        g1 = cria_gerador(32,1)
        for n in range(3):
            atualiza_estado(g1) 
        assert(gerador_para_str(g1) == "xorshift32(s=2647435461)")

class TestPublicCoordenada:

    #col needs to be str
    def test_cria_coordenada_arg1(self):
        with pytest.raises(ValueError,match="cria_coordenada: argumentos invalidos"):
            cria_coordenada(4,4) 
    
    #lin needs to be int
    def test_cria_coordenada_arg2(self):
        with pytest.raises(ValueError,match="cria_coordenada: argumentos invalidos"):
            cria_coordenada('A',4.0) 
    
    #col needs to be between 'A' and 'Z'
    def test_cria_coordenada_arg3(self):
        with pytest.raises(ValueError,match="cria_coordenada: argumentos invalidos"):
            cria_coordenada('a',4) 

    #lin needs to be between 1 and 99
    def test_cria_coordenada_arg4(self):
        with pytest.raises(ValueError,match="cria_coordenada: argumentos invalidos"):
            cria_coordenada('A',100) 
        
    
    def test_eh_coordenada_vdd(self):
        assert(eh_coordenada(('A',4)) == True)
    
    def test_eh_coordenada_typediff(self):
        assert(eh_coordenada(['A',4]) == False)
    
    def test_eh_coordenada_col_notstr(self):
        assert(eh_coordenada((4,4)) == False)
    
    def test_eh_coordenada_lin_notint(self):
        assert(eh_coordenada(('A',4.0)) == False)
    
    def test_eh_coordenada_mais2elementos(self):
        assert(eh_coordenada(('A',4,5)) == False)
    
    def test_coordenadas_iguais_vdd(self):
        assert(coordenadas_iguais(('A',4),('A',4)) == True)
    
    def test_coordenadas_iguais_typediff(self):
        assert(coordenadas_iguais(['A',4],('A',4)) == False)
    
    def test_coordenadas_para_str_1(self):
        assert(coordenada_para_str(('A',19)) == "A19")

    def test_coordenadas_para_str_2(self):
        assert(coordenada_para_str(('A',9)) == "A09")
         
    def test_str_para_coordenada_1(self):
        assert(str_para_coordenada("A09") == ('A',9))

    def test_str_para_coordenada_2(self):
        assert(str_para_coordenada("A19") == ('A',19))

    
    
    
    
    
    
