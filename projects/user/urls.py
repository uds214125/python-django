from django.contrib import admin
from django.urls import path
from . import views

# from django.conf import settings
# from django.conf.urls.defaults import handler404, handler500
# from app.views import error

urlpatterns = [
    path('', views.index, name="index"),
    path('signin',views.signin, name="signin"),
    path('signup',views.signup, name="signup"),
    path('home', views.home, name="home")
    # path('signout', name="signout")
]
# handler404 = error.error_handler
# handler500 = error.error_handler
# handler404 = 'app.views.404_view'
