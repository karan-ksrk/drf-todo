from django.urls import path
from .views import Register_User, Login_User, Logout_User


urlpatterns = [
    path('register/', Register_User, name="register"),
    path('login/', Login_User, name="login"),
    path('logout/', Logout_User, name="logout")
]