import requests
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

        assert "id" in data["data"]
        assert "email" in data["data"]
        assert "first_name" in data["data"]
        assert "last_name" in data["data"]
        logger.info("Estructura de la respuesta correcta")

        #NIVEL 4: CONTENIDO
        assert data["data"]["id"] == 2
        assert data["data"]["email"] == "janet.weaver@reqres.in"
        assert data["data"]["first_name"] == "Janet"
        assert data["data"]["last_name"] == "Weaver"
        logger.info("Datos dentro de la respuesta correctos")

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
        data = response.json()
        assert "id" in data
        assert "email" in data
        assert "first_name" in data
        assert "last_name" in data
        logger.info("Estructura de la respuesta correcta")

        #NIVEL 4: CONTENIDO
        assert data["email"] == usuario["email"]
        assert data["first_name"] == usuario["first_name"]
        assert data["last_name"] == usuario["last_name"]
        logger.info("Datos dentro de la respuesta correctos")

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
        data = response.json()
        assert "first_name" in data
        assert "last_name" in data
        logger.info("Estructura de la respuesta correcta")
        
        #NIVEL 4: CONTENIDO
        assert data["first_name"] == usuario["first_name"]
        assert data["last_name"] == usuario["last_name"]
        logger.info("Datos dentro de la respuesta correctos")
        
        #NIVEL 5: TIEMPO DE RESPUESTA
        assert response.elapsed.total_seconds() < 2
        logger.info("Tiempo de respuesta valido")

    except Exception:
        logger.exception("Error durante la prueba API borrar usuario")
        raise     