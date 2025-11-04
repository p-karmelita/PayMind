from flask import Flask, render_template
from dotenv import load_dotenv

# Import blueprints
from routes.health import health_bp
from routes.wallet_sets import wallet_sets_bp
from routes.wallets import wallets_bp
from routes.signing import signing_bp
from routes.transactions import transactions_bp
from routes.tokens import tokens_bp
from routes.modular_wallets import modular_wallets_bp
from routes.user_auth import user_auth_bp
from routes.pin_auth import pin_auth_bp
from routes.users import users_bp
from routes.compliance import compliance_bp
from routes.chatbot import chatbot_bp

app = Flask(__name__)
load_dotenv()

# Main documentation page
@app.route('/')
def index():
    return render_template('api_docs.html')

# Register blueprints
app.register_blueprint(health_bp)
app.register_blueprint(wallet_sets_bp)
app.register_blueprint(wallets_bp)
app.register_blueprint(signing_bp)
app.register_blueprint(transactions_bp)
app.register_blueprint(tokens_bp)
app.register_blueprint(modular_wallets_bp)
app.register_blueprint(user_auth_bp)
app.register_blueprint(pin_auth_bp)
app.register_blueprint(users_bp)
app.register_blueprint(compliance_bp)
app.register_blueprint(chatbot_bp)


if __name__ == '__main__':
    app.run(debug=True)
