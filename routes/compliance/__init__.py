from flask import Blueprint
import requests
import os

compliance_bp = Blueprint('compliance', __name__)


@compliance_bp.route('/screen_blockchain_address')
def screen_blockchain_address():
    url = "https://api.circle.com/v1/w3s/compliance/screening/addresses"
    idempotency_key = input("Enter idempotency key: ")
    address = input("Enter address: ")
    chain = input("Enter chain: ")
    payload = {
        "idempotencyKey": idempotency_key,
        "address": address,
        "chain": chain
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text
