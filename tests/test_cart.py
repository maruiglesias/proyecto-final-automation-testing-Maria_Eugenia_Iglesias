from pages.login_page import LoginPage
from pages.cart_page import CartPage

def test_cart(driver):
    login_page = LoginPage(driver)
    cart_page =CartPage(driver)

    driver.get("https://www.saucedemo.com/")
        
    login_page.login("standard_user","secret_sauce")

    #Anadir un producto
    cart_page.agregar_producto(driver)

    #Verificar contador en carrito
    assert cart_page.contador_carrito() == '1' 

    #Navegar al carrito de compras
    cart_page.ingresar_a_carrito()

    ##Comprobar que el producto fue anadido exitosamente
    #Validacion de un solo item agregado
    productos = cart_page.productos_en_cart()
    assert len(productos) == 1

    #Validacion de cantidad de producto 1
    assert cart_page.cantidad_producto_1() == '1'

    #Validacion del nombre del producto
    assert cart_page.nombre_producto_1() == "Sauce Labs Backpack"
    
    #Validacion del precio del producto
    assert cart_page.precio_producto_1() == "$29.99"