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