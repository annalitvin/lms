from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gen_teacher', views.gen_teacher, name='gen_teacher'),
    path('data_success', views.data_success, name='data_success'),
    path('teachers_list', views.teachers_list, name='teachers_list'),
    path('add_teacher', views.add_teacher, name='add_teacher'),
    path('edit_teacher/<int:id>', views.edit_teacher, name='edit_teacher'),
    path('delete_teacher/<int:id>', views.delete_teacher, name='delete_teacher')
]
