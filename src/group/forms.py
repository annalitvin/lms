from django.forms import ModelForm

from group.models import Group
from teacher.models import Teacher


class GroupAddForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
