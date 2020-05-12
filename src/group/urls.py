from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_group, name='add'),
    path('groups_list', views.groups_list, name='groups_list'),
    path('edit/<int:id>', views.edit_group, name='edit'),
    path('delete/<int:id>', views.delete_group, name='delete'),

]
