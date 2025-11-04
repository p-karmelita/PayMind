from flask import Blueprint
import requests
import os

pin_auth_bp = Blueprint('pin_auth', __name__)


@pin_auth_bp.route('/create_user')
def create_user():
    url = "https://api.circle.com/v1/w3s/users"
    ext_user_id = input("Enter external user id: ")
    payload = ext_user_id
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@pin_auth_bp.route('/create_user_token')
def create_user_token():
    url = "https://api.circle.com/v1/w3s/users/token"
    ext_user_id = input("Enter external user id: ")
    payload = ext_user_id
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@pin_auth_bp.route('/create_pin_challenge')
def create_pin_challenge():
    url = "https://api.circle.com/v1/w3s/user/pin"
    idempotency_key = input("Enter idempotency key: ")
    payload = idempotency_key
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@pin_auth_bp.route('/update_pin_challenge')
def update_pin_challenge():
    url = "https://api.circle.com/v1/w3s/user/pin"
    idempotency_key = input("Enter idempotency key: ")
    payload = idempotency_key
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.put(url, json=payload, headers=headers)
    return response.text


@pin_auth_bp.route('/restore_pin_challenge')
def restore_pin_challenge():
    url = "https://api.circle.com/v1/w3s/user/pin/restore"
    idempotency_key = input("Enter idempotency key: ")
    payload = idempotency_key
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text
