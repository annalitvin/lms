from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm

from student.models import Student


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAddForm(StudentBaseForm):
    groups_filter = Q()

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('phone_number').strip()
        email = cleaned_data.get('email').strip()

        is_student_exists = Student.objects.filter(Q(phone_number=phone_number) |
                                                   Q(email=email)).exists()
        if is_student_exists:
            error_massage = "Student not added. Student with such phone_number and email is exists! Try again:"
            raise ValidationError(error_massage)


class StudentEditForm(StudentBaseForm):
    pass
