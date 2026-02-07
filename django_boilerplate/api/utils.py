from .models import User

def get_user_from_token(request):
    print("HEADERS:", dict(request.headers))

    auth_header = request.headers.get("Authorization")
    print("AUTH HEADER:", auth_header)

    if not auth_header:
        return None

    try:
        token = auth_header.split(" ")[1]   # Bearer <token>
        return User.objects.get(token=token)
    except:
        return None
