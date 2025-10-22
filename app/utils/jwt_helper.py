import jwt
import datetime


def generate_jwt(user_id: int, secret: str, minutes: int = 60):
    payload = {"uid": user_id, "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=minutes)}
    return jwt.encode(payload, secret, algorithm="HS256")
