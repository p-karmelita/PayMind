from flask import Blueprint
import requests
import os

user_auth_bp = Blueprint('user_auth', __name__)


@user_auth_bp.route('/get_device_token_social')
def get_device_token_social():
    url = "https://api.circle.com/v1/w3s/users/social/token"
    idempotency_key = input("Enter idempotency key: ")
    device_id = input("Enter device id: ")
    payload = {
        "idempotencyKey": idempotency_key,
        "deviceId": device_id
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@user_auth_bp.route('/get_device_token_email')
def get_device_token_email():
    url = "https://api.circle.com/v1/w3s/users/email/token"
    idempotency_key = input("Enter idempotency key: ")
    device_id = input("Enter device id: ")
    email = input("Enter email: ")
    payload = {
        "idempotencyKey": idempotency_key,
        "deviceId": device_id,
        "email": email
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@user_auth_bp.route('/refresh_user_token')
def refresh_user_token():
    url = "https://api.circle.com/v1/w3s/users/token/refresh"
    idempotency_key = input("Enter idempotency key: ")
    refresh_token = input("Enter refresh token: ")
    device_id = input("Enter device id: ")
    payload = {
        "idempotencyKey": idempotency_key,
        "refreshToken": refresh_token,
        "deviceId": device_id
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@user_auth_bp.route('/resend_otp_email')
def resend_otp_email():
    url = "https://api.circle.com/v1/w3s/users/email/resendOTP"
    idempotency_key = input("Enter idempotency key: ")
    otp_token = input("Enter OTP token: ")
    email = input("Enter email: ")
    device_id = input("Enter device id: ")
    payload = {
        "idempotencyKey": idempotency_key,
        "otpToken": otp_token,
        "email": email,
        "deviceId": device_id
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('api_key')}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.text
