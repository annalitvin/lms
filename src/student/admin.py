from django.contrib import admin

from student.models import Student


class StudentAdminModel(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email')
    list_display = ('first_name', 'last_name', 'email', 'get_group_name', )
    list_select_related = ('group', )

    # почему-то не работает, хотя должно по идеи, в модели тоже пробовала получить атрибут, но ошибка аналогичная
    # https://stackoverflow.com/questions/163823/can-list-display-in-a-django-modeladmin-display-attributes-of-foreignkey-field
    # https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display

    def get_group_name(self, instance):
        print(instance.group.name)
        return instance.group.name


admin.site.register(Student, StudentAdminModel)
