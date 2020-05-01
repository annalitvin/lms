from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gen_student', views.gen_student, name='gen_student'),
    path('data_success', views.data_success, name='data_success')
]
