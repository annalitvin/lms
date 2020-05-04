from django.http import HttpResponse


def main(request):
    return HttpResponse("Get group by id using url: <strong> <a href='/teacher'>/teacher</a> </strong><br>"
                        "Generate students in database using url: <strong> <a href='/student'>/student</a> </strong>" +
                        "<br>Search students when all fields True using url: "
                        "<strong> <a href='/student/students_list/1'>/student/students_list/1</a> </strong><br>" +
                        "Search students when not all fields True using url: " +
                        "<strong> <a href='/student/students_list/2'>/student/students_list/2</a> </strong><br>"
                        "Get group by id using url: <strong> <a href='/group'>/group</a> </strong>",
                        status=200)
