from behave import given,when,then
from pages.login_page import LoginPage

@given("el usuario se encuentra en la pagina de login")
def step_usuario_en_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.abrir_pagina()

@when("ingresa en los campos de datos '{user}' y '{password}'")
def step_ingresar_credenciales(context,user,password):
    if user != 'VACIO':
        context.login_page.ingresar_usuario(user)
    if password != 'VACIO':
        context.login_page.ingresar_password(password)    

@when("hace click en el boton de login")
def step_click_login(context):
    context.login_page.hacer_click_login()

@then("deberia ingresar a la pagina de inventario")
def step_validar_login_exitoso(context):    
    assert "/inventory.html" in context.driver.current_url

@then("deberia aparecer un mensaje de error '{errormessage}'")    
def step_validar_mensaje_error(context, errormessage):
    error = context.login_page.obtener_mensaje_error()
    assert errormessage in error 