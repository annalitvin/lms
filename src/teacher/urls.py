from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate', views.gen_teacher, name='generate'),
    path('data_success', views.data_success, name='data_success'),
    path('list', views.teachers_list, name='list'),
    path('add', views.add_teacher, name='add'),
    path('edit/<int:id>', views.edit_teacher, name='edit'),
    path('delete/<int:id>', views.delete_teacher, name='delete')
]
