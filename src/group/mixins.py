
class GroupValidFormMixin:

    def form_valid(self, form):

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
                return self.render_to_response(self.get_context_data(form=form, error_massage=error_message,
                                                                     status=400))

        else:
            error_message = "Such specialty does not exist"
            return self.render_to_response(self.get_context_data(form=form, error_massage=error_message, status=400))

        response = super().form_valid(form)
        return response
