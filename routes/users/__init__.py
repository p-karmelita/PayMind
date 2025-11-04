from flask import Blueprint
import requests
import os

users_bp = Blueprint('users', __name__)


@users_bp.route('/list_users')
def list_users():
    url = "https://api.circle.com/v1/w3s/users"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@users_bp.route('/get_user_by_id')
def get_user_by_id():
    id = input("Enter user id: ")
    url = f"https://api.circle.com/v1/w3s/users/{id}"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@users_bp.route('/list_challenges')
def list_challenges():
    url = "https://api.circle.com/v1/w3s/user/challenges"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@users_bp.route('/get_challenge')
def get_challenge():
    id = input("Enter challenge id: ")
    url = f"https://api.circle.com/v1/w3s/user/challenges/{id}"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text


@users_bp.route('/get_user')
def get_user():
    url = "https://api.circle.com/v1/w3s/user"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.get(url, headers=headers)
    return response.text
