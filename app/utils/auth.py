from functools import wraps
from flask import request, current_app
import jwt


def auth_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization", "").replace("Bearer ", "").strip()
        if not token: return {"message": "Unauthorized"}, 401
        try:
            jwt.decode(token, current_app.config["JWT_SECRET"], algorithms=["HS256"])
        except Exception:
            return {"message": "Unauthorized"}, 401
        return fn(*args, **kwargs)

    return wrapper
