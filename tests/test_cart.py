from pages.login_page import LoginPage
from pages.cart_page import CartPage
from utils.logger import logger

def test_cart(driver):
    try:
        logger.info("Prueba carrito")
        login_page = LoginPage(driver)
        cart_page =CartPage(driver)

        driver.get("https://www.saucedemo.com/")
        logger.info("Pagina abierta correctamente")

        login_page.login("standard_user","secret_sauce")
        logger.info("Sesion iniciada correctamente")

        #Anadir un producto
        cart_page.agregar_producto(driver)
        logger.info("Agregando primer producto al carrito de compras")

        #Verificar contador en carrito
        assert cart_page.contador_carrito() == '1' 
        logger.info("Validacion del contador del carrito")

        #Navegar al carrito de compras
        cart_page.ingresar_a_carrito()
        logger.info("Navegacion al carrito para validar informacion dentro")

        ##Comprobar que el producto fue anadido exitosamente
        #Validacion de un solo item agregado
        productos = cart_page.productos_en_cart()
        assert len(productos) == 1
        logger.info("Cantidad de elementos en el carrito correcta")

        #Validacion de cantidad de producto 1
        assert cart_page.cantidad_producto_1() == '1'
        logger.info("Cantidad del producto uno correcta")
        
        #Validacion del nombre del producto
        assert cart_page.nombre_producto_1() == "Sauce Labs Backpack"
        logger.info("Nombre del producto agregado correcto")
   
        #Validacion del precio del producto
        assert cart_page.precio_producto_1() == "$29.99"
        logger.info("Precio del producto agregado correcto")

    except Exception:
        logger.exception("Error durante la prueba de carrito")
        raise        