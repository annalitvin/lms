from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
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
