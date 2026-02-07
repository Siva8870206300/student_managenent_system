def get_user_from_token(request):
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return None

    try:
        token = auth_header.split(" ")[1]
        return User.objects.get(token=token)
    except:
        return None
