from django.http.response import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from manager.forms.edit_task_form import EditTaskForm

__author__ = 'garfild'


class EditTask(FormView):
    template_name = 'manager/edit_task.html'
    form_class = EditTaskForm

    def form_valid(self, form):
        form.save()
        return HttpResponse('ثبت خدمت با موفقیت صورت گرفت.')


class ModelTaskList(ListView):
    pass
