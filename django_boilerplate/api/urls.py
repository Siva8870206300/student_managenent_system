from django.urls import path
from . import views

urlpatterns = [
    path("sign-up/", views.sign_up),
    path("sign-in/", views.sign_in),
    path("sign-out/", views.sign_out),
    path("update-user/<int:user_id>/", views.update_user),
    path("delete-user/<int:user_id>/", views.delete_user),
]
