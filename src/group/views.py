from django.db.models import Q
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from group.forms import GroupAddForm, GroupEditForm
from .models import Group


def index(request):

    id_group = request.GET.get('id')
    if id_group is not None:
        if not id_group.isdigit():
            return HttpResponse("'id' must be numeric and greatest when zero")

        id_group = int(id_group)
        if id_group == 0:
            return HttpResponse("'id' must be greatest when zero")
        try:
            group = Group.objects.get(pk=id_group)
        except Group.DoesNotExist:
            raise Http404("Group does not exist")
        return render(request, "group/index.html", {'group': group})
    return HttpResponse("Введите параметр id: ?id=n")


def groups_list(request):

    qs = Group.objects.all()

    name = request.GET.get('name')
    specialty = request.GET.get('specialty')
    course_name = request.GET.get('course_name')

    groups_filter = Q()

    if name:
        groups_filter |= Q(name=name)
    if specialty:
        groups_filter |= Q(specialty=specialty)
    if course_name:
        groups_filter |= Q(course_name=course_name)

    qs = qs.filter(groups_filter)

    return render(request, 'group/groups_list.html',
                  {'groups_list': qs, 'title': 'Group list'})


def add_group(request):

    add_group_template = 'group/add_group.html'

    if request.method == 'POST':
        form = GroupAddForm(request.POST)
        if form.is_valid():
            specialties = {
                "Python": ["Introduction Python", "Python", "Machine Learning and Deep Learning", "Django"],
                "SQL": ["Introduction SQL", "SQL"],
                "PHP": ["Introduction PHP", "PHP", "Symphony"]
            }
            specialty = form.cleaned_data.get('specialty').strip()
            course_name = form.cleaned_data.get('course_name').strip()
            if specialty in ["Python", "SQL", "PHP"]:
                if course_name not in specialties[specialty]:
                    error_message = "The course does not correspond to the specialty."
                    return render(request, add_group_template, {'form': form, "error_message": error_message},
                                  status=400)
            else:
                error_message = "Such specialty does not exist"
                return render(request, add_group_template, {'form': form, "error_message": error_message},
                              status=400)
            form.save()
            return HttpResponseRedirect(reverse('groups_list'))

    else:
        form = GroupAddForm()
    return render(request, add_group_template, {'form': form})


def edit_group(request, id):

    group_edit_template = 'group/group_edit.html'
    try:
        group = Group.objects.get(id=id)
    except Group.DoesNotExist:
        return HttpResponseNotFound(f"Group with id={id} doesn't exist")

    if request.method == 'POST':
        form = GroupEditForm(request.POST or None, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups_list'))
    else:
        form = GroupEditForm(instance=group)
    return render(request, group_edit_template, {'form': form, 'title': 'Edit student'})


def delete_group(request, id):

    group = get_object_or_404(Group, id=id)
    group.delete()
    return HttpResponseRedirect(reverse('groups_list'))
