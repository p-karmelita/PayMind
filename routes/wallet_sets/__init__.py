from flask import Blueprint
import requests
import os

wallet_sets_bp = Blueprint('wallet_sets', __name__)


@wallet_sets_bp.route("/create_wallet_set")
def create_wallet_set():
    url = "https://api.circle.com/v1/w3s/developer/walletSets"
    payload = {
        "entitySecretCiphertext": os.getenv("encrypted_entity_secret"),
        "idempotencyKey": "4c8bfed6-c32b-4af8-8679-ac1c59d2305e"
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@wallet_sets_bp.route("/get_wallet_set")
def get_wallet_set():
    id = input("Enter wallet set id: ")
    url = f"https://api.circle.com/v1/w3s/walletSets/{id}"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer TEST_API_KEY:a991429f6918f1f9971ae2ee8f2d116d:0ff55183b0cee2cff74ddcec86fad915"}
    response = requests.get(url, headers=headers)
    return response.text


@wallet_sets_bp.route("/get_all_wallet_sets")
def get_all_wallet_sets():
    url = "https://api.circle.com/v1/w3s/walletSets"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text
