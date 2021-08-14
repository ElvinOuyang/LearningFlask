"""Host subdomain script for api.py."""
from flask import Blueprint

subdomain_bp = Blueprint('subdomain', __name__)

@subdomain_bp.route('/hello/')
def hello():
    return "Hello from subdomain"