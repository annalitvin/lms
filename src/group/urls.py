from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index_group'),
    path('add_group', views.add_group, name='add_group'),
    path('groups_list', views.groups_list, name='groups_list'),
    path('edit_group/<int:id>', views.edit_group, name='edit_group'),
    path('delete_group/<int:id>', views.delete_group, name='delete_group'),

]
