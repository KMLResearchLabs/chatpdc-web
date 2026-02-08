import time

chat_sessions = {}

MAX_MESSAGES = 12
SESSION_TIMEOUT = 6000


def get_session(session_id: str):
    if session_id not in chat_sessions:
        chat_sessions[session_id] = {
            "messages": [],
            "last_seen": time.time()
        }
    else:
        chat_sessions[session_id]["last_seen"] = time.time()

    return chat_sessions[session_id]


def cleanup_sessions():
    now = time.time()
    expired = [
        sid for sid, data in chat_sessions.items()
        if now - data["last_seen"] > SESSION_TIMEOUT
    ]
    for sid in expired:
        del chat_sessions[sid]
