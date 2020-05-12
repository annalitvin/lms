from django.forms import ModelForm

from group.models import Group
from teacher.models import Teacher


class GroupBaseForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class GroupAddForm(GroupBaseForm):
    pass


class GroupEditForm(GroupBaseForm):
    pass
