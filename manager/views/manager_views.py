from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from manager.forms.edit_task_form import EditTaskForm
from service.models import TaskModel

__author__ = 'garfild'


class EditTask(FormView):
    template_name = 'manager/edit_task.html'
    form_class = EditTaskForm

    def form_valid(self, form):
        form.save()
        return redirect(reverse('manager:task_model_list'))


class ModelTaskList(ListView):
    model = TaskModel
    template_name = 'manager/show_task_models.html'
    context_object_name = 'task_models'

    def get_queryset(self):
        return TaskModel.objects.all()
