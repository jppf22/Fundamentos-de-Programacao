import pytest
import sys
from Minesweeper import *

class TestPublicGerador:

    # b tem que ser 32 ou 64 inteiros
    def test_cria_gerador_arg1(self):
        with pytest.raises(ValueError,matches="cria gerador: argumentos invalidos"):
            cria_gerador(40,1)

    def test_cria_gerador_arg2(self):
        with pytest.raises(ValueError,matches="cria gerador: argumentos invalidos"):
            cria_gerador(32.0,1)
    
    #s tem que ser inteiro positivo
    def test_cria_gerador_arg3(self):
        with pytest.raises(ValueError,matches="cria gerador: argumentos invalidos"):
            cria_gerador(32,-1)
    
    def test_cria_gerador_arg4(self):
        with pytest.raises(ValueError,matches="cria gerador: argumentos invalidos"):
            cria_gerador(32,1.0)
    