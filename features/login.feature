Feature: Inicio de sesion

    Background:
        Given el usuario se encuentra en la pagina de login

    Scenario: Login exitoso 
        When ingresa en los campos de datos 'standard_user' y 'secret_sauce'
        And hace click en el boton de login
        Then deberia ingresar a la pagina de inventario
    
    Scenario Outline: Login con credenciales invalidas 
        When ingresa en los campos de datos '<usuario>' y '<password>'
        And hace click en el boton de login
        Then deberia aparecer un mensaje de error '<Mensaje>'

        Examples:
        |usuario|password|Mensaje|
        |standard_user|123|Epic sadface: Username and password do not match any user in this service|
        |standarUser|secret_sauce|Epic sadface: Username and password do not match any user in this service|
        |standard_user|VACIO|Epic sadface: Password is required|
        |VACIO|secret_sauce|Epic sadface: Username is required|