import sender_stand_request
import data


# Función para obtener token
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    return user_response.json()["authToken"]


# Función para generar body
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body


# Validación positiva
def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(
        kit_body,
        auth_token
    )
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


# Validación negativa
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(
        kit_body,
        auth_token
    )
    assert response.status_code == 400

#Lista de comprobación
#1	El número permitido de caracteres (1):
def test_create_kit_1_character_in_name_get_success_response():
    positive_assert(get_kit_body("a"))

#2 	El número permitido de caracteres (511):
def test_create_kit_511_characters_in_name_get_success_response():
    positive_assert(get_kit_body(
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    ))

#3 	El número de caracteres es menor que la cantidad permitida (0):
def test_create_kit_0_characters_in_name_get_error_response():
    negative_assert_code_400(get_kit_body(""))

#4 	El número de caracteres es mayor que la cantidad permitida (512):
def test_create_kit_512_characters_in_name_get_error_response():
    negative_assert_code_400(get_kit_body(
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcDE"
    ))

#5  Se permiten caracteres especiales:
def test_create_kit_special_characters_in_name_get_success_response():
    positive_assert(get_kit_body("\"№%@\","))

#6  Se permiten espacios:
def test_create_kit_spaces_in_name_get_success_response():
    positive_assert(get_kit_body(" A Aaa "))

#7 	Se permiten números:
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert(get_kit_body("123"))

#8 	El parámetro no se pasa en la solicitud:
def test_create_kit_no_name_parameter_get_error_response():
    kit_body = {}
    negative_assert_code_400(kit_body)

#9 	Se ha pasado un tipo de parámetro diferente (número):
def test_create_kit_number_type_name_get_error_response():
    kit_body = {
        "name": 123
    }
    negative_assert_code_400(kit_body)
    

