# Proyecto Urban Grocers - Automatización de Pruebas API
## Descripción
Este proyecto contiene pruebas automatizadas para validar la creación de kits mediante una API utilizando Python, PyCharm, Requests y Pytest.

Las pruebas incluyen validaciones positivas y negativas del parámetro `name` al crear un kit de producto.

---

# Tecnologías utilizadas

- Python
- PyCharm
- Pytest
- Librería Requests

---

# Casos de prueba cubiertos

Las pruebas validan:

- Longitud mínima permitida
- Longitud máxima permitida
- Longitud menor a la permitida
- Longitud mayor a la permitida
- Caracteres especiales
- Espacios
- Números
- Parámetro ausente
- Tipo de dato incorrecto

# Autor
Proyecto final desarrollado como parte del Sprint:
Introducción a la Automatización de Pruebas QA

---

# Estructura del proyecto

```bash
qa-project/
│
├── configuration.py
├── data.py
├── sender_stand_request.py
├── create_kit_name_kit_test.py
└── .venv
