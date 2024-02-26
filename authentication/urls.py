from django.urls import path 
from .views import signup, login, home, cartPage, logoutUser

urlpatterns = [
    path("signup/", signup),
    path("login/", login),
    path("", home),
    path("cart/", cartPage),
    path("logout/", logoutUser)
]