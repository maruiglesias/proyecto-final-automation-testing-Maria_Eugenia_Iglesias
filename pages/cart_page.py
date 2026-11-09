from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver    
   
    def agregar_producto(self,driver):
        inventory_page = InventoryPage(driver)
        
        productos = inventory_page.obtener_productos()
        return (productos[0].find_element(By.XPATH,"//button[text()='Add to cart']")).click()

    def contador_carrito(self):
        contador_cart = self.driver.find_element(By.XPATH,"//span[@data-test='shopping-cart-badge']").text
        return contador_cart

    def ingresar_a_carrito(self):
        return self.driver.find_element(By.CSS_SELECTOR,"[data-test='shopping-cart-link']").click()

    def productos_en_cart(self):
        productos_cart = self.driver.find_elements(By.CLASS_NAME,"cart_item")
        return productos_cart

    def cantidad_producto_1(self):
        productos_cart = self.productos_en_cart()
        return productos_cart[0].find_element(By.CLASS_NAME,"cart_quantity").text
            
    def nombre_producto_1(self):
        productos_cart = self.productos_en_cart()
        return productos_cart[0].find_element(By.CLASS_NAME,"inventory_item_name").text

    def precio_producto_1(self):
        productos_cart = self.productos_en_cart()
        return productos_cart[0].find_element(By.CLASS_NAME,"inventory_item_price").text
               
