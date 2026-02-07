from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
import json
import uuid 
from .models import User




def home(request):
    return JsonResponse({
        "message": "Django API running successfully"
    })


def get_user_from_token(request):
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return None

    try:
        token = auth_header.split(" ")[1] 
        return User.objects.get(token=token)
    except (IndexError, User.DoesNotExist):
        return None



@csrf_exempt
def sign_up(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST method required"}, status=405)

    try:
        body = request.body.decode("utf-8")
        data = json.loads(body)

        
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        age = data.get("age")
        gender = data.get("gender")


        if not all([name, email, password, age, gender]):
            return JsonResponse({"error": "All fields are required"}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already exists"}, status=400)

        user = User.objects.create(
            name=name,
            email=email,
            password=make_password(str(password)),
            age=int(age),
            gender=gender
        )

        return JsonResponse(
            {"message": "User created successfully", "id": user.id},
            status=201
        )

    except Exception as e:
        return JsonResponse(
            {"error": str(e), "type": type(e).__name__},
            status=500
        )



@csrf_exempt
def sign_in(request):
    if request.method != "GET":
        return JsonResponse(
            {"error": "GET method required"},
            status=405
        )

    email = request.GET.get("email")
    password = request.GET.get("password")

    if not email or not password:
        return JsonResponse(
            {"error": "Email and password are required"},
            status=400
        )

    try:
        user = User.objects.get(email=email)

        if not check_password(str(password), user.password):
            return JsonResponse(
                {"error": "Invalid email or password"},
                status=401
            )

        # Generate token
        user.token = str(uuid.uuid4())
        user.save()

        return JsonResponse({
            "message": "Login successful",
            "token": user.token,
            "user_id": user.id,
            "name": user.name
        })

    except User.DoesNotExist:
        return JsonResponse(
            {"error": "Invalid email or password"},
            status=401
        )



@csrf_exempt
def update_user(request, user_id):
    if request.method != "PUT":
        return JsonResponse({"error": "PUT method required"}, status=405)

    auth_user = get_user_from_token(request)
    if not auth_user:
        return JsonResponse({"error": "Unauthorized"}, status=401)


    if auth_user.id != user_id:
        return JsonResponse(
            {"error": "You cannot update another user"},
            status=403
        )

    data = json.loads(request.body)

    auth_user.name = data.get("name", auth_user.name)
    auth_user.age = data.get("age", auth_user.age)
    auth_user.email = data.get("email", auth_user.email)

    if "password" in data:
        auth_user.password = make_password(data["password"])

    auth_user.gender = data.get("gender", auth_user.gender)
    auth_user.save()

    return JsonResponse({"message": "User updated successfully"})


@csrf_exempt
def delete_user(request, user_id):
    if request.method != "DELETE":
        return JsonResponse(
            {"error": "Only DELETE method allowed"},
            status=405
        )


    auth_user = get_user_from_token(request)
    if not auth_user:
        return JsonResponse(
            {"error": "Unauthorized"},
            status=401
        )

    
    if auth_user.id != user_id:
        return JsonResponse(
            {"error": "You cannot delete another user"},
            status=403
        )

    auth_user.delete()
    return JsonResponse({
        "message": "User deleted successfully"
    })



@csrf_exempt
def sign_out(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "POST method required"},
            status=405
        )

    auth_user = get_user_from_token(request)
    if not auth_user:
        return JsonResponse(
            {"error": "Unauthorized"},
            status=401
        )

    # Invalidate token
    auth_user.token = None
    auth_user.save()

    return JsonResponse({
        "message": "Logout successful"
    })
