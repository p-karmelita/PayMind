from flask import Blueprint
from circle.web3 import utils

health_bp = Blueprint('health', __name__)


@health_bp.route("/health")
def health():
    api_instance = utils.configurations.HealthApi()
    response = api_instance.ping()
    return response.json()
