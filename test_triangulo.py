import pytest
from triangulo import checktriangle

def test_caso1_escaleno():
    assert checktriangle(6, 5, 10) == "Triangulo escaleno"

def test_caso2_equilatero():
    assert checktriangle(3, 3, 3) == "Triangulo equilatero"

def test_caso3_isosceles():
    assert checktriangle(4, 4, 5) == "Triangulo isosceles"

def test_caso4_no_triangulo():
    assert checktriangle(7, 2, 3) == "No es un triangulo"

def test_caso5_no_triangulo_cero():
    assert checktriangle(4, 3, 0) == "No es un triangulo"

def test_isosceles_bc():
    assert checktriangle(8, 5, 5) == "Triangulo isosceles"

def test_isosceles_ac():
    assert checktriangle(5, 8, 5) == "Triangulo isosceles"

def test_no_es_triangulo_suma_igual():
    assert checktriangle(2, 2, 4) == "No es un triangulo"

def test_no_es_triangulo_lado_mayor_primero():
    assert checktriangle(10, 2, 2) == "No es un triangulo"

def test_no_es_triangulo_lado_mayor_segundo():
    assert checktriangle(2, 10, 2) == "No es un triangulo"

def test_no_es_triangulo_lado_negativo():
    assert checktriangle(-1, 5, 5) == "No es un triangulo"