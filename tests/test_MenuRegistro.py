import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from register_menu import MenuRegistro


"""
Test validar_username()

"""

def test_Test1ValidarUsernameCorto():
    menu = MenuRegistro()
    válido, msg = menu.validar_username("jn")

    assert válido == False
    assert msg == "El username debe tener al menos 3 caracteres"

def test_Test1ValidarUsernameCaracteres():
    menu = MenuRegistro()
    válido, msg = menu.validar_username("jose*/")

    assert válido == False

    assert msg == "El username solo puede contener letras, números y guión bajo"

def test_Test3ValidarUsernameCorrecto():
    menu = MenuRegistro()
    válido, msg = menu.validar_username("jskd123")

    assert válido == True
    assert msg == ""

    ##assert msg == "El username solo puede contener letras, números y guión bajo"      ###Error

"""
Test validar_contraseña()

"""

def test_Test1ValidarContraseñaCorta():
    menu = MenuRegistro()
    valido, msg = menu.validar_contraseña("Abc!")
    assert valido == False
    assert msg == "La contraseña debe tener al menos 8 caracteres"

def test_Test2ValidarContraseñaCaracter():
    menu = MenuRegistro()
    valido, msg = menu.validar_contraseña("Absc1234")
    
    assert valido == False
    assert msg == "La contraseña debe contener al menos un carácter especial (!@#$%...)"

def test_Test3ValidarContraseñaCorrecta():
    menu = MenuRegistro()
    valido, msg = menu.validar_contraseña("Asdfg1234**")

    ###valido, msg = menu.validar_contraseña("asdfg123468")      ###Error

    assert valido == True
    assert msg == ""

