from .models import User


def create_user(data):
    # Business logic only
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    age = data.get("age")
    gender = data.get("gender")
    token = uuid.uuid4()
    
    if not name or not age or not gender:
        raise ValueError("name, age and gender are required")

    return User.objects.create(
        name=name,
        email=email,
        password=password,
        age=age,
        gender=gender,
        token=uuid.uuid4(),

    )


def update_user_by_id(user_id, data):
    try:
        user = User.objects.get(id=user_id)

        if "name" in data:
            user.name = data["name"]
        if "age" in data:
            user.age = data["age"]
        if "gender" in data:
            user.gender = data["gender"]

        user.save()
        return user

    except User.DoesNotExist:
        return None
        

def delete_user_controller(user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return {
            "message": "User deleted successfully",
            "status": 200
        }
    except User.DoesNotExist:
        return {
            "error": "User not found",
            "status": 404
        }
