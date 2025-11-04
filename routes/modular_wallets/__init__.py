from flask import Blueprint
import requests
import os

modular_wallets_bp = Blueprint('modular_wallets', __name__)


@modular_wallets_bp.route('/list_transfers')
def list_transfers():
    url = "https://api.circle.com/v1/w3s/buidl/transfers"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@modular_wallets_bp.route('/retrieve_transfer')
def retrieve_transfer():
    id = input("Enter transfer id: ")
    url = f"https://api.circle.com/v1/w3s/buidl/transfers/{id}"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@modular_wallets_bp.route('/list_user_operations')
def list_user_operations():
    url = "https://api.circle.com/v1/w3s/buidl/userOps"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@modular_wallets_bp.route('/retrieve_user_operation')
def retrieve_user_operation():
    id = input("Enter user operation id: ")
    url = f"https://api.circle.com/v1/w3s/buidl/userOps/{id}"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@modular_wallets_bp.route('/get_buidl_wallet_balances')
def get_buidl_wallet_balances():
    id = input("Enter wallet id: ")
    url = f"https://api.circle.com/v1/w3s/buidl/wallets/{id}/balances"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@modular_wallets_bp.route('/get_buidl_wallet_nfts')
def get_buidl_wallet_nfts():
    id = input("Enter wallet id: ")
    url = f"https://api.circle.com/v1/w3s/buidl/wallets/{id}/nfts"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@modular_wallets_bp.route('/get_buidl_wallet_balances_by_blockchain')
def get_buidl_wallet_balances_by_blockchain():
    blockchain = input("Enter blockchain: ")
    address = input("Enter address: ")
    url = f"https://api.circle.com/v1/w3s/buidl/wallets/{blockchain}/{address}/balances"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@modular_wallets_bp.route('/get_buidl_wallet_nfts_by_blockchain')
def get_buidl_wallet_nfts_by_blockchain():
    blockchain = input("Enter blockchain: ")
    address = input("Enter address: ")
    url = f"https://api.circle.com/v1/w3s/buidl/wallets/{blockchain}/{address}/nfts"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text
