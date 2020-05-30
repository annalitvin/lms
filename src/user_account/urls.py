from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('register', views.CreateUserAccountView.as_view(), name='registration'),
]
