# Selenium Automation Project

Proyecto de automatización de pruebas utilizando Selenium WebDriver y Pytest - Curso QA Automation - Talento Tech

## Tecnologías utilizadas

- Python
- Selenium
- Pytest
- Git
- GitHub

## Instalación

```python
pip install pytest
```
```python
pip install selenium
```
```python
pip install pytest-html
```
```python
pip install pytest-check
```
```python
pip install pytest-rerunfailures
```
```python
pip install behave
```
## Ejecución de pruebas
## Pruebas pytest
```python
pytest
```
## Pruebas BDD
```python
behave
```

## Casos de prueba
### Pruebas UI
- Login exitoso
- Validacion de mensaje de error en Login con credenciales invalidas 
- Validacion pagina Inventory
- Agregar productos al carrito y validar su contenido
### Pruebas API
- Obtener usuario
- Crear usuario
- Borrar usuario
- Actualizar usuario
### Pruebas BDD
- Login exitoso
- Validacion de mensaje de error en Login con credenciales invalidas 

## Estructura del proyecto
├── pages/
│ ├── login_page.py
| ├── inventory_page.py
│ └── cart_page.py
├── tests/
│ ├── test_login.py
| ├── test_inventory.py
│ ├── test_cart.py
│ └── test_api.py
├── utils/
│ ├── logger.py
│ └── reader.py
├── reports/
│ ├──reporte.html
│ └── screenshots/
├── logs/
├── data/
├── features/
│ ├──steps/
| |  └──login_steps.py
│ ├──environment.py
│ └──login.feature
└── README.md

## Autor

Maria Eugenia Iglesias