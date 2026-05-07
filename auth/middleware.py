from auth.jwt_handler import verify_token


def get_user_from_request(request):
    token = request.headers.get("Authorization")

    if not token:
        return None

    return verify_token(token.replace("Bearer ", ""))