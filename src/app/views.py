from django.http import HttpResponse


def main(request):
    return HttpResponse("Get teacher by id using url: <strong> <a href='/teacher'>/teacher</a> </strong><br>" +
                        "Added teacher: <strong> <a href='/teacher/add'>/teacher/add</a> </strong>"
                        + "<br>" +
                        "Search teachers: <strong> <a href='/teacher/list'>/teacher/list/</a></strong>"
                        + "<br>" +
                        "Generate students in database using url: <strong> <a href='/student'>/student</a> </strong>"
                        + "<br>" +
                        "Search students when all fields True using url: " +
                        "<strong> <a href='/student/list/1'>/student/list/1</a> </strong><br>" +
                        "Search students when not all fields True using url: " +
                        "<strong> <a href='/student/list/2'>/student/list/2</a> </strong><br>" +
                        "Added student: <strong> <a href='/student/add'>/student/add</a> </strong>"
                        + "<br>" +
                        "Get group by id using url: <strong> <a href='/group'>/group</a> </strong><br>" +
                        "Added group: <strong> <a href='/group/add'>/group/add</a> </strong>" +
                        "<br>" +
                        "Search groups: <strong> <a href='/group/groups_list'>/group/groups_list/</a></strong>",
                        status=200)
