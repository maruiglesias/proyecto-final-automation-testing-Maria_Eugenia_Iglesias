Feature: Inicio de sesion

    Scenario: Login exitoso
        Given el usuario se encuentra en la pagina de login
        When ingresa en los campos de datos 'standard_user' y 'secret_sauce'
        And hace click en el boton de login
        Then deberia ingresar a la pagina de inventario

    Scenario: Login con credenciales invalidas
        Given el usuario se encuentra en la pagina de login
        When ingresa en los campos de datos 'standard_user' y '123'
        And hace click en el boton de login
        Then deberia aparecer un mensaje de error