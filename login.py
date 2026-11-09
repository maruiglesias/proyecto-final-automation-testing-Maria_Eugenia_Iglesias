import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.login import login

#Test Login Exitoso
def test_loginexitoso():
    try:
        driver = login("standard_user","secret_sauce")

        #validar el URL despues del login
        assert "/inventory.html" in driver.current_url

        #validar encabezado en la pagina inventory con espera explicita requerida por el proyecto  
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'header_label')))

        encabezado = driver.find_element(By.CLASS_NAME,"app_logo")
        assert encabezado.text == 'Swag Labs'

        #Validar texto
        titulo = driver.find_element(By.CSS_SELECTOR,"[data-test='title']")
        assert titulo.text == 'Products'
        
    finally:
        driver.quit()

#Test Login Fallido
def test_loginFail():
    try:
        driver = login("standard_user","123")
    
        #validar mensaje de error
        errorMessage = driver.find_element(By.CSS_SELECTOR,"[data-test='error']")
        assert errorMessage.text == 'Epic sadface: Username and password do not match any user in this service'
            
    finally:
        driver.quit()