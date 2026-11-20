import requests

def test_obtener_usuario():
    url="https://reqres.in/api/users/2"

    header = {
        "x-api-key": "reqres_30304c3dafc04758b8db4299ac4def16"
    }

    response = requests.get(url,headers=header)

    #NIVEL 1: STATUS CODE
    codigo = response.status_code
    assert codigo == 200

    #NIVEL 2: HEADERS
    assert "application/json" in response.headers["Content-Type"]

    #NIVEL 3: ESTRUCTURA
    data = response.json()

    assert isinstance(data,dict) #validar que el contenido es un diccionario
    assert "data" in data
    assert isinstance(data["data"],dict)

    assert "id" in data["data"]
    assert "email" in data["data"]
    assert "first_name" in data["data"]
    assert "last_name" in data["data"]

    #NIVEL 4: CONTENIDO
    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"
    assert data["data"]["first_name"] == "Janet"
    assert data["data"]["last_name"] == "Weaver"

    #NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2

def test_crear_usuario():
    url="https://reqres.in/api/users"
    
    header = {
        "x-api-key": "reqres_30304c3dafc04758b8db4299ac4def16"
    }

    usuario = {
        "email": "testapi@testtest.com",
        "first_name": "Maria",
        "last_name": "Test_test"
    }

    response = requests.post(url,headers=header,json=usuario)

    #NIVEL 1: STATUS CODE
    codigo = response.status_code
    assert codigo == 201

    #NIVEL 2: HEADERS
    assert "application/json" in response.headers["Content-Type"]

    #NIVEL 3: ESTRUCTURA
    data = response.json()
    assert "id" in data
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data

    #NIVEL 4: CONTENIDO
    assert data["email"] == usuario["email"]
    assert data["first_name"] == usuario["first_name"]
    assert data["last_name"] == usuario["last_name"]

    #NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2

def test_eliminar_usuario():    
    url="https://reqres.in/api/users/2"
    
    header = {
        "x-api-key": "reqres_30304c3dafc04758b8db4299ac4def16"
    }
    
    response = requests.delete(url,headers=header)

    #NIVEL 1: STATUS CODE
    codigo = response.status_code
    assert codigo == 204
    
    #NIVEL 2: HEADERS
    assert len(response.content) == 0

def test_actualizar_usuario():

    url="https://reqres.in/api/users/2"
    
    header = {
        "x-api-key": "reqres_30304c3dafc04758b8db4299ac4def16"
    }

    usuario = {
            "first_name": "Maria",
            "last_name": "Test_test"
        }

    response = requests.patch(url,headers=header,json=usuario)

    #NIVEL 1: STATUS CODE
    codigo = response.status_code
    assert codigo == 200

    #NIVEL 2: HEADERS
    assert "application/json" in response.headers["Content-Type"]

    #NIVEL 3: ESTRUCTURA
    data = response.json()
    assert "first_name" in data
    assert "last_name" in data

    #NIVEL 4: CONTENIDO
    assert data["first_name"] == usuario["first_name"]
    assert data["last_name"] == usuario["last_name"]

    #NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2
    
    