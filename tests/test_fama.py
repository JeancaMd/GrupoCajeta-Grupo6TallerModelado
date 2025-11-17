import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fama import SalonFama

@pytest.fixture
def salon_fama():
    sf = SalonFama()
    sf.screen = None 
    sf.running = False
    return sf


def test_Test1FormatearTiempo(salon_fama):
    resultado = salon_fama.formatear_tiempo(75)
    
    assert resultado == "01:10" 

def test_Test2FormatearTiempo(salon_fama):
    resultado = salon_fama.formatear_tiempo(0)
    
    assert resultado == "00:00"

def test_Test3FormatearTiempo(salon_fama):
    with pytest.raises(ValueError):
        salon_fama.formatear_tiempo(-5)


def test_Test1HayTiemposRegistrados(salon_fama):
    salon_fama.tiempos = [("Gabo", 120), ("Jeanca", 150)]
    resultado = salon_fama.hay_tiempos_registrados()
    
    assert resultado == True

def test_Test2HayTiemposRegistrados(salon_fama):
    salon_fama.tiempos = []
    resultado = salon_fama.hay_tiempos_registrados()
    
    assert resultado == False

def test_Test3HayTiemposRegistrados(salon_fama):
    salon_fama.tiempos = None
    resultado = salon_fama.hay_tiempos_registrados()
    
    assert resultado == False