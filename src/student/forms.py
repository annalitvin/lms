from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm

from student.models import Student


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAddForm(StudentBaseForm):

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('phone_number').strip()
        email = cleaned_data.get('email').strip()

        is_student_exists = Student.objects.filter(Q(phone_number=phone_number) |
                                                   Q(email=email)).exists()
        if is_student_exists:
            error_massage = "Student not added. Student with such phone_number and email is exists! Try again:"
            raise ValidationError(error_massage)
        return self.cleaned_data


class StudentEditForm(StudentBaseForm):

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)

    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email').strip()

        is_email_exists = Student.objects.filter(email=email).exclude(pk=self.pk).exists()

        if is_email_exists:
            error_massage = "Student not added. Student with such email is exists! Try again:"
            raise ValidationError(error_massage)
        return email

    def clean(self):

        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name').strip()
        last_name = cleaned_data.get('last_name').strip()

        if first_name == last_name:
            error_massage = "First name and last name must be different"
            raise ValidationError(error_massage)
        return self.cleaned_data
