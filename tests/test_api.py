import requests
import pytest_check as check
from utils.logger import logger

def test_obtener_usuario(base_url,headers):
    try:
        logger.info("Prueba API - Obtener Usuario")

        url= f"{base_url}/users/2"
        response = requests.get(url,headers=headers)

        #NIVEL 1: STATUS CODE
        codigo = response.status_code
        assert codigo == 200
        logger.info("Status Code correcto")

        #NIVEL 2: HEADERS
        assert "application/json" in response.headers["Content-Type"]
        logger.info("Validacion de headers correcta")

        #NIVEL 3: ESTRUCTURA
        data = response.json()

        assert isinstance(data,dict) #validar que el contenido es un diccionario
        assert "data" in data
        assert isinstance(data["data"],dict)

        logger.info("Validacion de la estructura de la respuesta")
        check.is_in("id",data["data"]) #assert "id" in data["data"]
        check.is_in("email",data["data"]) #assert "email" in data["data"]
        check.is_in("first_name",data["data"]) #assert "first_name" in data["data"]
        check.is_in("last_name",data["data"]) #assert "last_name" in data["data"]

        #NIVEL 4: CONTENIDO
        logger.info("Validacion de los datos dentro de la respuesta")
        check.equal(data["data"]["id"],2) # assert data["data"]["id"] == 2
        check.equal(data["data"]["email"],"janet.weaver@reqres.in") # assert data["data"]["email"] == "janet.weaver@reqres.in"
        check.equal(data["data"]["first_name"],"Janet") # assert data["data"]["first_name"] == "Janet"
        check.equal(data["data"]["last_name"],"Weaver") # assert data["data"]["last_name"] == "Weaver"

        #NIVEL 5: TIEMPO DE RESPUESTA
        assert response.elapsed.total_seconds() < 2
        logger.info("Tiempo de respuesta valido")

    except Exception:
        logger.exception("Error durante la prueba API obtener usuario")
        raise    

def test_crear_usuario(base_url,headers):
    try:
        logger.info("Prueba API - Crear Usuario")
        
        url=f"{base_url}/users"
        
        usuario = {
            "email": "testapi@testtest.com",
            "first_name": "Maria",
            "last_name": "Test_test"
        }

        response = requests.post(url,headers=headers,json=usuario)

        #NIVEL 1: STATUS CODE
        codigo = response.status_code
        assert codigo == 201
        logger.info("Status Code correcto")

        #NIVEL 2: HEADERS
        assert "application/json" in response.headers["Content-Type"]
        logger.info("Validacion de headers correcta")

        #NIVEL 3: ESTRUCTURA
        logger.info("Validacion de estructura de la respuesta")
        data = response.json()
        check.is_in("id",data) #assert "id" in data
        check.is_in("email",data) #assert "email" in data
        check.is_in("first_name",data) #assert assert "first_name" in data
        check.is_in("last_name",data) #assert "last_name" in data
        
        #NIVEL 4: CONTENIDO
        logger.info("Validacion de los datos dentro de la respuesta")
        check.equal(data["email"],usuario["email"]) #assert data["email"] == usuario["email"]
        check.equal(data["first_name"],usuario["first_name"]) #assert data["first_name"] == usuario["first_name"]
        check.equal(data["last_name"],usuario["last_name"]) #assert data["last_name"] == usuario["last_name"]
        
        #NIVEL 5: TIEMPO DE RESPUESTA
        assert response.elapsed.total_seconds() < 2
        logger.info("Tiempo de respuesta valido")

    except Exception:
        logger.exception("Error durante la prueba API crear usuario")
        raise    

def test_eliminar_usuario(base_url,headers): 
    try:   
        url=f"{base_url}/users/2"
        
        response = requests.delete(url,headers=headers)

        #NIVEL 1: STATUS CODE
        codigo = response.status_code
        assert codigo == 204
        logger.info("Status Code correcto")
    
        #NIVEL 2: HEADERS
        assert "Content-Type" not in response.headers
        logger.info("Validacion de headers correcta")

        #NIVEL 3 Y 4: ESTRUCTURA Y CONTENIDO
        assert len(response.content) == 0
        logger.info("Estructura y contenido de la respuesta correcta - sin datos")

        #NIVEL 5: TIEMPO DE RESPUESTA
        assert response.elapsed.total_seconds() < 2
        logger.info("Tiempo de respuesta valido")

    except Exception:
        logger.exception("Error durante la prueba API borrar usuario")
        raise  

def test_actualizar_usuario(base_url,headers):
    try:
        url=f"{base_url}/users/2"

        usuario = {
                "first_name": "Maria",
                "last_name": "Test_test"
            }

        response = requests.patch(url,headers=headers,json=usuario)

        #NIVEL 1: STATUS CODE
        codigo = response.status_code
        assert codigo == 200
        logger.info("Status Code correcto")

        #NIVEL 2: HEADERS
        assert "application/json" in response.headers["Content-Type"]
        logger.info("Validacion de headers correcta")

        #NIVEL 3: ESTRUCTURA
        logger.info("Validacion de estructura de la respuesta")
        data = response.json()
        check.is_in("first_name",data) #assert "first_name" in data
        check.is_in("last_name",data) #assert "last_name" in data
        
        #NIVEL 4: CONTENIDO
        logger.info("Validacion de los datos dentro de la respuesta")
        check.equal(data["first_name"],usuario["first_name"]) #assert data["first_name"] == usuario["first_name"]
        check.equal(data["last_name"],usuario["last_name"]) #assert data["last_name"] == usuario["last_name"]
        
        #NIVEL 5: TIEMPO DE RESPUESTA
        assert response.elapsed.total_seconds() < 2
        logger.info("Tiempo de respuesta valido")

    except Exception:
        logger.exception("Error durante la prueba API actualizar usuario")
        raise     