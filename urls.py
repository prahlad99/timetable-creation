from django.urls import path
from .import views


urlpatterns = [

    path('register/',views.register,name="register"),
    path('login/',views.loginp,name="login"),
    path('logout/',views.logoutuser,name="logout"),
    path('',views.time,name="time"),
]
