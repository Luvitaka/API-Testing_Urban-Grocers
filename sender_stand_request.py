import Configuration
import requests
import data

# Crear usuario
def post_new_user(body):
    return requests.post(
        Configuration.URL_SERVICE + Configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )


# Crear kit
def post_new_client_kit(kit_body, auth_token):
    current_headers = data.headers.copy()
    current_headers["Authorization"] = "Bearer " + auth_token
    return requests.post(
        Configuration.URL_SERVICE + Configuration.CREATE_KIT_PATH,
        json=kit_body,
        headers=current_headers
    )
