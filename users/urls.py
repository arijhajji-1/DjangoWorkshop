from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', loginView, name='login'),
]
