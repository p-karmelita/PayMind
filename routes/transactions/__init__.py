from flask import Blueprint
import requests
import os

transactions_bp = Blueprint('transactions', __name__)


@transactions_bp.route('/list_transactions')
def list_transactions():
    url = "https://api.circle.com/v1/w3s/transactions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@transactions_bp.route('/get_transaction')
def get_transaction():
    id = input("Enter transaction id: ")
    url = f"https://api.circle.com/v1/w3s/transactions/{id}"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@transactions_bp.route('/get_lowest_nonce_transaction')
def get_lowest_nonce_transaction():
    url = "https://api.circle.com/v1/w3s/transactions/lowestNonceTransaction"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@transactions_bp.route('/create_transfer_transaction')
def create_transfer_transaction():
    url = "https://api.circle.com/v1/w3s/developer/transactions/transfer"
    idempotency_key = input("Enter idempotency key: ")
    destination_address = input("Enter destination address: ")
    payload = {
        "idempotencyKey": idempotency_key,
        "destinationAddress": destination_address,
        "entitySecretCiphertext": os.getenv("encrypted_entity_secret")
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@transactions_bp.route('/validate_address')
def validate_address():
    url = "https://api.circle.com/v1/w3s/transactions/validateAddress"
    address = input("Enter address: ")
    blockchain = input("Enter blockchain: ")
    payload = {
        "address": address,
        "blockchain": blockchain
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@transactions_bp.route('/estimate_fee_contract_execution')
def estimate_fee_contract_execution():
    url = "https://api.circle.com/v1/w3s/transactions/contractExecution/estimateFee"
    contract_address = input("Enter contract address: ")
    payload = {"contractAddress": contract_address}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@transactions_bp.route('/estimate_fee_transfer')
def estimate_fee_transfer():
    url = "https://api.circle.com/v1/w3s/transactions/transfer/estimateFee"
    amounts = input("Enter amounts (comma-separated): ")
    destination_address = input("Enter destination address: ")
    payload = {
        "amounts": amounts.split(","),
        "destinationAddress": destination_address
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@transactions_bp.route('/create_contract_execution_transaction')
def create_contract_execution_transaction():
    url = "https://api.circle.com/v1/w3s/developer/transactions/contractExecution"
    idempotency_key = input("Enter idempotency key: ")
    contract_address = input("Enter contract address: ")
    payload = {
        "idempotencyKey": idempotency_key,
        "contractAddress": contract_address,
        "entitySecretCiphertext": os.getenv("encrypted_entity_secret")
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@transactions_bp.route('/create_wallet_upgrade_transaction')
def create_wallet_upgrade_transaction():
    url = "https://api.circle.com/v1/w3s/developer/transactions/walletUpgrade"
    idempotency_key = input("Enter idempotency key: ")
    new_sca_core = input("Enter new SCA core: ")
    wallet_id = input("Enter wallet id: ")
    payload = {
        "idempotencyKey": idempotency_key,
        "newScaCore": new_sca_core,
        "entitySecretCiphertext": os.getenv("encrypted_entity_secret"),
        "walletId": wallet_id
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@transactions_bp.route('/cancel_transaction')
def cancel_transaction():
    id = input("Enter transaction id: ")
    url = f"https://api.circle.com/v1/w3s/developer/transactions/{id}/cancel"
    idempotency_key = input("Enter idempotency key: ")
    payload = {
        "idempotencyKey": idempotency_key,
        "entitySecretCiphertext": os.getenv("encrypted_entity_secret")
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@transactions_bp.route('/accelerate_transaction')
def accelerate_transaction():
    id = input("Enter transaction id: ")
    url = f"https://api.circle.com/v1/w3s/developer/transactions/{id}/accelerate"
    idempotency_key = input("Enter idempotency key: ")
    payload = {
        "idempotencyKey": idempotency_key,
        "entitySecretCiphertext": os.getenv("encrypted_entity_secret")
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@transactions_bp.route('/create_challenge_transfer')
def create_challenge_transfer():
    url = "https://api.circle.com/v1/w3s/user/transactions/transfer"
    idempotency_key = input("Enter idempotency key: ")
    destination_address = input("Enter destination address: ")
    wallet_id = input("Enter wallet id: ")
    payload = {
        "idempotencyKey": idempotency_key,
        "destinationAddress": destination_address,
        "walletId": wallet_id
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@transactions_bp.route('/create_challenge_accelerate_transaction')
def create_challenge_accelerate_transaction():
    id = input("Enter transaction id: ")
    url = f"https://api.circle.com/v1/w3s/user/transactions/{id}/accelerate"
    idempotency_key = input("Enter idempotency key: ")
    payload = idempotency_key
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@transactions_bp.route('/create_challenge_cancel_transaction')
def create_challenge_cancel_transaction():
    id = input("Enter transaction id: ")
    url = f"https://api.circle.com/v1/w3s/user/transactions/{id}/cancel"
    idempotency_key = input("Enter idempotency key: ")
    payload = idempotency_key
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@transactions_bp.route('/create_challenge_contract_execution')
def create_challenge_contract_execution():
    url = "https://api.circle.com/v1/w3s/user/transactions/contractExecution"
    idempotency_key = input("Enter idempotency key: ")
    contract_address = input("Enter contract address: ")
    wallet_id = input("Enter wallet id: ")
    payload = {
        "idempotencyKey": idempotency_key,
        "contractAddress": contract_address,
        "walletId": wallet_id
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@transactions_bp.route('/create_challenge_wallet_upgrade')
def create_challenge_wallet_upgrade():
    url = "https://api.circle.com/v1/w3s/user/transactions/walletUpgrade"
    idempotency_key = input("Enter idempotency key: ")
    new_sca_core = input("Enter new SCA core: ")
    wallet_id = input("Enter wallet id: ")
    payload = {
        "idempotencyKey": idempotency_key,
        "newScaCore": new_sca_core,
        "walletId": wallet_id
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text
