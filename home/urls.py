from django.urls import path
from . import views
urlpatterns = [
    path('',views.signin , name="login"),
    path('register',views.register, name="register"),
    path('home',views.home, name="home"),
    path('signout',views.signout, name="signout"),
    path('activate/<uidb64>/<token>',views.activate, name="activate"),
]
