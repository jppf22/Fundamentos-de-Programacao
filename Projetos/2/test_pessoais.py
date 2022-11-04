import pytest
import sys
from Minesweeper import *

class TestPublicGerador:

    # b tem que ser 32 ou 64 inteiros
    def test_cria_gerador_arg1(self):
        with pytest.raises(ValueError,match="cria gerador: argumentos invalidos"):
            cria_gerador(40,1)

    def test_cria_gerador_arg2(self):
        with pytest.raises(ValueError,match="cria gerador: argumentos invalidos"):
            cria_gerador(32.0,1)
    
    #s tem que ser inteiro positivo
    def test_cria_gerador_arg3(self):
        with pytest.raises(ValueError,match="cria gerador: argumentos invalidos"):
            cria_gerador(32,-1)
    
    def test_cria_gerador_arg4(self):
        with pytest.raises(ValueError,match="cria gerador: argumentos invalidos"):
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
        assert(geradores_iguais(cria_gerador(32,1),cria_gerador(32,1)) == True)
    
    def test_geradores_iguais_tiposdiff(self):
        assert(geradores_iguais([32,1],(32,1)) == False)
    
    def test_geradores_iguais_seeddiff(self):
        assert(geradores_iguais(cria_gerador(32,2),cria_gerador(32,1)) == False)
    
    def test_geradores_iguais_bitdiff(self):
        assert(geradores_iguais(cria_gerador(32,1),cria_gerador(64,1)) == False)
    
    def test_gerador_para_str_vdd(self):
        assert(gerador_para_str(cria_gerador(32,1)) == "xorshift32(s=1)")
    
    def test_geradpr_para_str_seedgrande(self):
        g1 = cria_gerador(32,1)
        for n in range(3):
            atualiza_estado(g1) 
        assert(gerador_para_str(g1) == "xorshift32(s=2647435461)")



class TestPublicParcela:

    def test_cria_parcela(self):
        assert(cria_parcela() == ["tapada",False])
    
    def test_cria_copia_parcela(self):
        p1 = cria_parcela()
        p2 = cria_copia_parcela(p1)
        assert(id(p1) != id(p2))
    
    def test_eh_parcela_falso(self):
        assert(eh_parcela(["outroestado",False]) == False)
    
    def test_parcelas_iguais_default(self):
        assert(parcelas_iguais(cria_parcela(),cria_parcela()) == True)

    def test_parcelas_iguais_vdd(self):
        p1 = ["tapada",True]
        p2 = ["tapada",True]
        assert((p1 == p2) == True)
    
    def test_parcelas_iguais_diff(self):
        p1 = ["tapada",False]
        p2 = ["marcada",True]
        assert((p1 == p2) == False)
    
    



    