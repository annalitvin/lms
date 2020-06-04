from django.contrib import admin

from student.models import Student


class StudentAdminModel(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email')
    list_display = ('first_name', 'last_name', 'email', 'get_group_name', )
    list_select_related = ('group', )

    # почему-то не работает, хотя должно по идеи, в модели тоже пробовала получить атрибут, но ошибка аналогичная
    # https://stackoverflow.com/questions/163823/can-list-display-in-a-django-modeladmin-display-attributes-of-foreignkey-field
    # https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display

    # решено, но все таки не ясно почему до этого не работало, когда проверку 'if instance.group:' не делалась

    def get_group_name(self, instance):
        if instance.group:
            return instance.group.name

    get_group_name.short_description = 'Group name'


admin.site.register(Student, StudentAdminModel)
