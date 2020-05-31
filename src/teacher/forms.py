from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm

from teacher.models import Teacher


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherAddForm(TeacherBaseForm):

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('phone_number').strip()
        email = cleaned_data.get('email').strip()

        is_teacher_exists = Teacher.objects.filter(Q(phone_number=phone_number) |
                                                   Q(email=email)).exists()
        if is_teacher_exists:
            error_massage = "Teacher not added. Teacher with such phone_number or email is exists! Try again:"
            raise ValidationError(error_massage)


class TeacherEditForm(TeacherBaseForm):
    pass
