from django.forms import ModelForm

from teacher.models import Teacher


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherAddForm(TeacherBaseForm):
    pass


class TeacherEditForm(TeacherBaseForm):
    pass
