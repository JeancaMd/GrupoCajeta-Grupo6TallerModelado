import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from database import GrupoCajetaDB

@pytest.fixture
def grupo_cajeta_db():
    db = GrupoCajetaDB()
    db.connection = None
    db.cursor = None
    return db


def test_Test1HashContraseña(grupo_cajeta_db):
    resultado = grupo_cajeta_db.hash_contraseña("password123")
    
    assert resultado is not None

def test_Test2HashContraseña(grupo_cajeta_db):
    resultado1 = grupo_cajeta_db.hash_contraseña("misma_contraseña")
    resultado2 = grupo_cajeta_db.hash_contraseña("misma_contraseña")
    
    assert resultado1 != resultado2

def test_Test3HashContraseña(grupo_cajeta_db):
    with pytest.raises(AttributeError):
        grupo_cajeta_db.hash_contraseña(None)


def test_Test1VerificarHashed(grupo_cajeta_db):
    hashed = grupo_cajeta_db.hash_contraseña("test_password")
    resultado = grupo_cajeta_db.verificar_hashed("test_password", hashed)
    
    assert resultado == True

def test_Test2VerificarHashed(grupo_cajeta_db):
    hashed = grupo_cajeta_db.hash_contraseña("password123")
    resultado = grupo_cajeta_db.verificar_hashed("wrong_password", hashed)
    
    assert resultado == False

def test_Test3VerificarHashed(grupo_cajeta_db):
    resultado = grupo_cajeta_db.verificar_hashed("password", "no_es_un_hash_valido")
    
    assert resultado == False