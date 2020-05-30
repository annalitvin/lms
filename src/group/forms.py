from django.core.exceptions import ValidationError
from django.forms import ModelForm

from group.models import Group
from teacher.models import Teacher


class GroupBaseForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class GroupAddForm(GroupBaseForm):

    def clean(self):
        cleaned_data = super().clean()

        specialties = {
            "Python": ["Introduction Python", "Python", "Machine Learning and Deep Learning", "Django"],
            "SQL": ["Introduction SQL", "SQL"],
            "PHP": ["Introduction PHP", "PHP", "Symphony"]
        }

        specialty = cleaned_data.get('specialty').strip()
        course_name = cleaned_data.get('course_name').strip()
        if specialty in ["Python", "SQL", "PHP"]:
            if course_name not in specialties[specialty]:
                error_message = "The course does not correspond to the specialty."
                self.add_error('course_name', error_message)

        else:
            error_message = "Such specialty does not exist"
            self.add_error('specialty', error_message)


class GroupEditForm(GroupBaseForm):
    pass
