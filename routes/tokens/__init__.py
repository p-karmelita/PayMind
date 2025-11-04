from flask import Blueprint
import requests
import os

tokens_bp = Blueprint('tokens', __name__)


@tokens_bp.route('/get_token_details')
def get_token_details():
    id = input("Enter token id: ")
    url = f"https://api.circle.com/v1/w3s/tokens/{id}"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text
