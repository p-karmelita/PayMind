from flask import Blueprint, jsonify, request
import sys
import os

# Add parent directory to path to import chatbot module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from AI_Agent.chatbot import get_ai_reply

chatbot_bp = Blueprint('chatbot', __name__)


@chatbot_bp.route('/api/chat', methods=['POST'])
def api_chat():
    """Chatbot backend endpoint used by static/chatbot.js
    Accepts JSON: {message: str, history: [[role, content], ...]}
    Returns JSON: {ok: bool, reply: str, history: same_format}
    """
    data = request.get_json(silent=True) or {}
    message = str((data.get('message') or '')).strip()
    history = data.get('history') or []
    if not message:
        return jsonify({"ok": False, "reply": "Brak wiadomości do przetworzenia."}), 400

    # Try to get AI reply; fall back to a deterministic message if unavailable
    reply = get_ai_reply(message, history)  # may be None if no API key or error
    if not reply:
        reply = (
            "Thank you for your message. I'm sorry, I don't have an answer for you yet."
        )

    # Update history on the server side for convenience to keep UI simple
    try:
        history = (history + [['user', message], ['assistant', reply]])[-20:]
    except Exception:
        history = [['user', message], ['assistant', reply]]

    return jsonify({"ok": True, "reply": reply, "history": history}), 200
