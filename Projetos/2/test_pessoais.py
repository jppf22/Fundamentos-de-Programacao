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
    
    def test_limpa_parcela(self):
        p1 = cria_parcela()
        assert(id(limpa_parcela(p1)) == id(p1) and p1 == ["limpa",False])

    def test_marca_parcela(self):
        p1 = cria_parcela()
        assert(id(marca_parcela(p1)) == id(p1) and p1 == ["marcada",False])
    
    def test_desmarca_parcela(self):
        p1 = cria_parcela()
        assert(id(desmarca_parcela(p1)) == id(p1) and p1 == ["tapada",False])

    def test_esconde_mina(self):
        p1 = cria_parcela()
        assert(id(esconde_mina(p1)) == id(p1) and p1 == ["tapada",True])

    def test_eh_parcela_falso(self):
        assert(eh_parcela(["outroestado",False]) == False)
    
    def test_eh_parcela_vdd(self):
        assert(eh_parcela(["tapada",True]) == True)
    
    def test_parcelas_iguais_default(self):
        assert(parcelas_iguais(cria_parcela(),cria_parcela()) == True)

    def test_parcelas_iguais_vdd(self):
        p1 = ["tapada",True]
        p2 = ["tapada",True]
        assert(parcelas_iguais(p1,p2) == True)
    
    def test_parcelas_iguais_diff(self):
        p1 = ["tapada",False]
        p2 = ["marcada",True]
        assert(parcelas_iguais(p1,p2) == False)
    
    def test_parcela_para_str_LimpaComMina(self):
        assert(parcela_para_str((["limpa",True])) == "X")
    
    def test_parcela_para_str_LimpaSemMina(self):
        assert(parcela_para_str((["limpa",False])) == "?")
    
    def test_parcela_para_str_Tapada(self):
        assert(parcela_para_str((["tapada",True])) == "#")
    
    def test_parcela_para_str_Marcada(self):
        assert(parcela_para_str((["marcada",True])) == "@")
    
 
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
    
    def test_eh_coordenada_lin_fora_campo1(self):
        assert(eh_coordenada(('A',0)) == False)
    
    def test_eh_coordenada_lin_fora_campo2(self):
        assert(eh_coordenada(('A',100)) == False)
    
    def test_eh_coordenada_col_fora_campo1(self):
        assert(eh_coordenada(('@',1)) == False)
    
    def test_eh_coordenada_col_fora_campo2(self):
        assert(eh_coordenada(('[',1)) == False)
    
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

    def test_obtem_coordenadas_vizinhas_cantoSE(self):
        c1 = cria_coordenada('A', 1)
        t = obtem_coordenadas_vizinhas(c1)
        assert ('B01', 'B02', 'A02') == tuple(coordenada_para_str(p) for p in t)

    def test_obtem_coordenadas_vizinhas_cantoSD(self):
        c1 = cria_coordenada('Z', 1)
        t = obtem_coordenadas_vizinhas(c1)
        assert ('Z02', 'Y02', 'Y01') == tuple(coordenada_para_str(p) for p in t)
    
    def test_obtem_coordenadas_vizinhas_cantoIE(self):
        c1 = cria_coordenada('A', 99)
        t = obtem_coordenadas_vizinhas(c1)
        assert ('A98', 'B98', 'B99') == tuple(coordenada_para_str(p) for p in t)
    
    def test_obtem_coordenadas_vizinhas_cantoID(self):
        c1 = cria_coordenada('Z', 99)
        t = obtem_coordenadas_vizinhas(c1)
        assert ('Y98','Z98', 'Y99') == tuple(coordenada_para_str(p) for p in t)
    
    def test_obtem_coordenadas_vizinhas_Esquerda(self):
        c1 = cria_coordenada('A', 22)
        t = obtem_coordenadas_vizinhas(c1)
        assert ('A21','B21', 'B22','B23','A23') == tuple(coordenada_para_str(p) for p in t)
    
    def test_obtem_coordenadas_vizinhas_Direita(self):
        c1 = cria_coordenada('Z', 22)
        t = obtem_coordenadas_vizinhas(c1)
        assert ('Y21','Z21', 'Z23','Y23','Y22') == tuple(coordenada_para_str(p) for p in t)

    def test_obtem_coordenadas_vizinhas_Cima(self):
        c1 = cria_coordenada('E', 1)
        t = obtem_coordenadas_vizinhas(c1)
        assert ('F01','F02', 'E02','D02','D01') == tuple(coordenada_para_str(p) for p in t)
    
    def test_obtem_coordenadas_vizinhas_Baixo(self):
        c1 = cria_coordenada('E', 99)
        t = obtem_coordenadas_vizinhas(c1)
        assert ('D98','E98', 'F98','F99','D99') == tuple(coordenada_para_str(p) for p in t)
    
    def test_obtem_coordenadas_vizinhas_CasoNormal(self):
        c1 = cria_coordenada('E', 5)
        t = obtem_coordenadas_vizinhas(c1)
        assert ('D04','E04','F04','F05','F06','E06','D06','D05') == tuple(coordenada_para_str(p) for p in t)
    
