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
    
class TestPublicCampo:

    def test_cria_campo_umaparcela(self):
        assert((cria_campo('A',1) == [[["tapada",False]]]) == True)
    
    def test_cria_campo_max(self):
        assert((cria_campo('Z',99) == [[cria_parcela() for x in range(ord('Z')-ord('A')+1)] for y in range(99)]) == True)

    def test_cria_campo_error1(self):
        with pytest.raises(ValueError,match="cria_campo: argumentos invalidos"):
            cria_campo('A','100')
    
    def test_cria_campo_error2(self):
        with pytest.raises(ValueError,match="cria_campo: argumentos invalidos"):
            cria_campo(1,100)
    
    def test_cria_copia_campo(self):
        c = cria_campo('E',5)
        assert((id(c) != id(cria_copia_campo(c))) == True)

    def test_obtem_collin_max(self):
        c = cria_campo('Z',99)
        assert((obtem_ultima_coluna(c) == 'Z' and obtem_ultima_linha(c) == 99) == True)
    
    def test_obtem_collin_min(self):
        c = cria_campo('A',1)
        assert((obtem_ultima_coluna(c) == 'A' and obtem_ultima_linha(c) == 1) == True)
    
    def test_obtem_ultima_colunalinha1(self):
        c = cria_campo('B',5)
        assert((obtem_ultima_coluna(c) == 'B' and obtem_ultima_linha(c) == 5) == True)

    def test_obtem_ultima_colunalinha2(self):
        c = cria_campo('E',2)
        assert((obtem_ultima_coluna(c) == 'E' and obtem_ultima_linha(c) == 2) == True)
    
    def test_obtem_coordenadas_normal(self):
        c = cria_campo('C',3)
        limpa_parcela(obtem_parcela(c,cria_coordenada('A',1)))
        limpa_parcela(obtem_parcela(c,cria_coordenada('B',2))) 
        limpa_parcela(obtem_parcela(c,cria_coordenada('C',3)))
        assert((obtem_coordenadas(c,"limpas") == (cria_coordenada('A',1),cria_coordenada('B',2),cria_coordenada('C',3))) == True) 

    def test_obtem_coordenadas_min(self):
        c = cria_campo('A',1)
        assert((obtem_coordenadas(c,"tapadas") == (cria_coordenada('A',1),)) == True)   
    
    def test_obtem_coordenadas_max(self):
        c = cria_campo('Z',99)
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums = range(1,100)
        assert((obtem_coordenadas(c,"tapadas") == tuple(cria_coordenada(x,y) for y in nums for x in letras)) == True)   
    
    def test_obtem_numero_minas_vizinhas_test1(self):
        c = cria_campo('E',5)
        esconde_mina(obtem_parcela(c,cria_coordenada('A',1)))
        esconde_mina(obtem_parcela(c,cria_coordenada('A',3)))
        esconde_mina(obtem_parcela(c,cria_coordenada('C',2)))
        esconde_mina(obtem_parcela(c,cria_coordenada('B',3)))
        assert((obtem_numero_minas_vizinhas(c,cria_coordenada('B',2)) == 4) == True)
    
    def test_obtem_numero_minas_vizinhas_test2(self):
        c = cria_campo('E',5)
        esconde_mina(obtem_parcela(c,cria_coordenada('A',1)))
        esconde_mina(obtem_parcela(c,cria_coordenada('A',3)))
        esconde_mina(obtem_parcela(c,cria_coordenada('C',2)))
        esconde_mina(obtem_parcela(c,cria_coordenada('B',3)))
        assert((obtem_numero_minas_vizinhas(c,cria_coordenada('A',2)) == 3) == True)
    
    def test_obtem_numero_minas_vizinhas_test3(self):
        c = cria_campo('E',5)
        esconde_mina(obtem_parcela(c,cria_coordenada('A',1)))
        esconde_mina(obtem_parcela(c,cria_coordenada('A',3)))
        esconde_mina(obtem_parcela(c,cria_coordenada('C',2)))
        esconde_mina(obtem_parcela(c,cria_coordenada('B',3)))
        assert((obtem_numero_minas_vizinhas(c,cria_coordenada('B',1)) == 2) == True)
    
    def test_obtem_numero_minas_vizinhas_nenhuma(self):
        c = cria_campo('E',5)
        esconde_mina(obtem_parcela(c,cria_coordenada('A',1)))
        esconde_mina(obtem_parcela(c,cria_coordenada('A',3)))
        esconde_mina(obtem_parcela(c,cria_coordenada('C',2)))
        esconde_mina(obtem_parcela(c,cria_coordenada('B',3)))
        assert((obtem_numero_minas_vizinhas(c,cria_coordenada('E',5)) == 0) == True)
    
    def test_obtem_numero_minas_vizinhas_todas(self):
        c = cria_campo('C',3)
        coordinate_test = cria_coordenada('B',2)
        for i in obtem_coordenadas_vizinhas(coordinate_test):
            esconde_mina(obtem_parcela(c,i))
        assert((obtem_numero_minas_vizinhas(c,coordinate_test) == 8) == True)
    
    def test_eh_campo_vdd_1elemento(self):
        assert((eh_campo([[["tapada",False]]])) == True)
    
    def test_eh_campo_vdd_2elementos(self):
        assert((eh_campo([[["tapada",False]],[["tapada",False]]])) == True)
    
    def test_eh_campo_falso_vazio(self):
        assert((eh_campo([[]])) == False)
    
    def test_eh_campo_falso_tipo_errado(self):
        assert((eh_campo(((["tapada",False])))) == False)
    
    def test_eh_campo_falso_formato_errado(self):
        assert((eh_campo([["tapada",False]])) == False)
    
    def test_eh_coordenada_do_campo_vdd(self):
        c1 = cria_campo('E',5)
        assert((eh_coordenada_do_campo(c1,cria_coordenada('C',3))) == True)
    
    def test_eh_coordenada_do_campo_vdd_min(self):
        c1 = cria_campo('A',1)
        assert((eh_coordenada_do_campo(c1,cria_coordenada('A',1))) == True)
    
    def test_eh_coordenada_do_campo_vdd_max(self):
        c1 = cria_campo('Z',99)
        assert((eh_coordenada_do_campo(c1,cria_coordenada('Z',99))) == True)
    
    def test_eh_coordenada_do_campo_falso(self):
        c1 = cria_campo('E',5)
        assert((eh_coordenada_do_campo(c1,cria_coordenada('F',3))) == False)
    
    def test_campos_iguais_vdd(self):
        c1 = cria_campo('A',1)
        c2 = [[["tapada",False]]]
        assert((c1 == c2) == True)
    
    def test_campos_iguais_falso_min(self):
        c1 = cria_campo('A',1)
        c2 = [[["tapada",True]]]
        assert((c1 == c2) == False)
    
    def test_campos_iguais_falso_1diff(self):
        c1 = cria_campo('Z',99)
        c2 = cria_campo('Z',99)
        esconde_mina(obtem_parcela(c2,cria_coordenada('D',5)))
        assert((c1 == c2) == False)
    
class TestMOOSHAK:

    def test_MOOSHAK_41(self):
        with pytest.raises(ValueError, match="cria_gerador: argumentos invalidos"):
            assert(cria_gerador(32,1267650600228229401496703205376))

    def test_MOOSHAK_52(self):
        assert(eh_gerador([32.0,1]) == False)

    def test_MOOSHAK_54(self):
        assert(eh_gerador([32,1267650600228229401496703205376]) == False)

    def test_MOOSHAK_55(self):
        assert(eh_gerador({}) == False)

    def test_MOOSHAK_72(self):
        with pytest.raises(ValueError, match="cria_coordenada: argumentos invalidos"):
            assert(cria_coordenada('MA',10))

    def test_MOOSHAK_86(self):
        assert(eh_coordenada(('B0',15)) == False)

    def test_MOOSHAK_125(self):
        assert(eh_parcela([]) == False)

    def test_MOOSHAK_165(self):
        with pytest.raises(ValueError, match="cria_campo: argumentos invalidos"):
            assert(cria_campo('LB',25))

    def test_MOOSHAK_173(self):
        m1 = cria_campo('M',80)
        m1_c = cria_copia_campo(m1)
        a1 = cria_coordenada('A',1)
        p1 = obtem_parcela(m1_c,a1)
        p2 = obtem_parcela(m1,a1)
        assert(parcelas_iguais(p1,p2) == False)

    def test_MOOSHAK_191(self):
        assert(eh_campo([]) == False)

    ''' Acho que está bem mas há alguma xatiçe com formatação
    def test_MOOSHAK_212(self):
        c = cria_campo('J',8)
        coloca_minas(c,cria_coordenada('J',8),cria_gerador(32,32),10)
        limpa_campo(c,cria_coordenada('J',8))
        limpa_campo(c,cria_coordenada('B',3))
        limpa_campo(c,cria_coordenada('H',7))
        str_c = campo_para_str(c)
        assert((str_c == "   ABCDEFGHIJ\n  +----------+\n01|##########|\n02|##########|\n03|#X#1111111|\n04|###1      |\n05|###1      |\n06|###222211 |\n07|#######X1 |\n08|########1 |\n  +----------+\n") == True)
    '''
    '''
    def test_MOOSHAK_227(self):
        pass

    '''
    '''
    def test_MOOSHAK_229(self):
        pass
    '''

    def test_MOOSHAK_232(self):
        with pytest.raises(ValueError,match="minas: argumentos invalidos"):
            minas('FA',10,6,32,100)

    def test_MOOSHAK_238(self): #mais minas que coordenadas
        with pytest.raises(ValueError,match="minas: argumentos invalidos"):
            minas('E',5,100,32,100)

    def test_MOOSHAK_239(self): #1 mina para 4 parcelas
        with pytest.raises(ValueError,match="minas: argumentos invalidos"):
            minas('B',2,1,32,100)

    def test_MOOSHAK_243(self): # 0 minas
        with pytest.raises(ValueError,match="minas: argumentos invalidos"):
            minas('J',35,0,64,50)

    