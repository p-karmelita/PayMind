from flask import Blueprint
import requests
import os

signing_bp = Blueprint('signing', __name__)


@signing_bp.route('/sign_message')
def sign_message():
    url = "https://api.circle.com/v1/w3s/developer/sign/message"
    payload = {
        "message": "I agree with this transfer",
        "entitySecretCiphertext": os.getenv("encrypted_entity_secret")
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@signing_bp.route('/sign_typed_data')
def sign_typed_data():
    url = "https://api.circle.com/v1/w3s/developer/sign/typedData"
    data = input("Enter data: ")
    payload = {
        f"{data}": "{ \"types\": { \"Data\": [{ \"name\": \"dummy\", \"type\": \"string\" }],\"EIP712Domain\":[{ \"name\": \"name\", \"type\": \"string\" },{ \"name\": \"chainId\", \"type\": \"uint256\" }]}, \"domain\": { \"name\": \"Test\", \"chainId\": 1337 }, \"primaryType\": \"Data\", \"message\": { \"dummy\": \"dummy\" }}",
        "entitySecretCiphertext": os.getenv("encrypted_entity_secret"),
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@signing_bp.route('/sign_transaction')
def sign_transaction():
    url = "https://api.circle.com/v1/w3s/developer/sign/transaction"
    payload = { "entitySecretCiphertext": os.getenv("encrypted_entity_secret")}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@signing_bp.route('/sign_delegate_action')
def sign_delegate_action():
    url = "https://api.circle.com/v1/w3s/developer/sign/delegateAction"
    walletId = input("Enter wallet id: ")
    unsigneDelegateAction = input("Enter unsigned delegate action: ")
    payload = {
        "walletId": f"{walletId}",
        "unsignedDelegateAction": f"{unsigneDelegateAction}",
        "entitySecretCiphertext": os.getenv("encrypted_entity_secret")
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@signing_bp.route('/create_challenge_sign_message')
def create_challenge_sign_message():
    url = "https://api.circle.com/v1/w3s/user/sign/message"
    wallet_id = input("Enter wallet id: ")
    message = input("Enter message: ")
    payload = {
        "walletId": wallet_id,
        "message": message
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@signing_bp.route('/create_challenge_sign_typed_data')
def create_challenge_sign_typed_data():
    url = "https://api.circle.com/v1/w3s/user/sign/typedData"
    wallet_id = input("Enter wallet id: ")
    data = input("Enter data: ")
    payload = {
        "walletId": wallet_id,
        "data": data
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@signing_bp.route('/create_challenge_sign_transaction')
def create_challenge_sign_transaction():
    url = "https://api.circle.com/v1/w3s/user/sign/transaction"
    wallet_id = input("Enter wallet id: ")
    payload = {"walletId": wallet_id}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text
