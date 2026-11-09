from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    driver.get("https://www.saucedemo.com/")
    
    login_page.login("standard_user","secret_sauce")
    
    #Validacion titulo pagina
    assert driver.title == 'Swag Labs'

    #Validacion presencia de productos
    productos = inventory_page.obtener_productos()

    assert len(productos) > 0

    #Validacion nombre/precio del primer producto
    assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"

    assert inventory_page.obtener_precio_primer_producto() == "$29.99"

    #Validar que elementos importantes de la interfaz estén presentes
    # Validacion de menu visible
    assert inventory_page.menu_visible() 
    
    #Validar carrito visible
    assert inventory_page.carrito_visible()

    #Validar Filtro visible 
    assert inventory_page.filtro_visible()
