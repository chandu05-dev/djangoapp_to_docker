from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("signupsuccess",views.signupsuccess, name="signupsuccess"),
    path("register", views.register_request, name="register"),
    path("mylogin", views.mylogin, name="mylogin"),
    path("logout", views.logout_request, name= "logout"),
]