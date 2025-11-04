from flask import Blueprint
import requests
import os

wallets_bp = Blueprint('wallets', __name__)


@wallets_bp.route("/create_wallet")
def create_wallet():
    url = "https://api.circle.com/v1/w3s/developer/wallets"
    payload = {
        "idempotencyKey": "4c8bfed6-c32b-4af8-8679-ac1c59d2305e",
        "blockchain": ["MATIC-AMOY"],
        "entitySecretCiphertext": os.getenv("encrypted_entity_secret"),
        "walletSetId": "e671ac4a-97d6-5b38-8264-cb814a5f8c7a"
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@wallets_bp.route("/list_wallets")
def list_wallets():
    url = "https://api.circle.com/v1/w3s/wallets"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@wallets_bp.route("/retrieve_wallet")
def retrieve_wallet():
    id = input("Enter wallet set id: ")
    url = f"https://api.circle.com/v1/w3s/wallets/{id}"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@wallets_bp.route("/update_wallet")
def update_wallet():
    id = input("Enter wallet set id: ")
    url = f"https://api.circle.com/v1/w3s/wallets/{id}"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.put(url, headers=headers)
    return response.text


@wallets_bp.route("/list_wallets_with_balances")
def list_wallets_with_balances():
    url = "https://api.circle.com/v1/w3s/developer/wallets/balances"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@wallets_bp.route("/get_token_balance_for_a_wallet")
def get_token_balance_for_a_wallet():
    id = input("Enter wallet id: ")
    url = f"https://api.circle.com/v1/w3s/wallets/{id}/balances"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@wallets_bp.route('/derive_a_wallet')
def derive_a_wallet():
    id = input("Enter wallet id: ")
    blockchain = input("Enter blockchain: ")
    url = f"https://api.circle.com/v1/w3s/developer/wallets/{id}/blockchains/{blockchain}"
    payload = {"refId": "custom_ref_id"}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.put(url, json=payload, headers=headers)
    return response.text


@wallets_bp.route('/get_nfts_for_a_wallet')
def get_nfts_for_a_wallet():
    id = input("Enter wallet id: ")
    url = f"https://api.circle.com/v1/w3s/wallets/{id}/nfts"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@wallets_bp.route('/create_user_wallets')
def create_user_wallets():
    url = "https://api.circle.com/v1/w3s/user/wallets"
    idempotency_key = input("Enter idempotency key: ")
    blockchains = input("Enter blockchains (comma-separated): ")
    payload = {
        "idempotencyKey": idempotency_key,
        "blockchains": blockchains.split(",")
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text
