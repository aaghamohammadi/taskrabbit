from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from manager.forms.edit_task_form import EditTaskForm
from manager.forms.tasker_registration_form import TaskerRegistrationForm
from service.models import TaskModel
from user.models import Customer

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


class TaskerVerification(ListView):
    model = Customer
    template_name = 'manager/verification.html'
    context_object_name = 'Taskers'

    def get_queryset(self):
        return Customer.objects.all()


class DeleteTasker(View):
    def post(self, request, **kwargs):
        tasker_id = kwargs.pop('tasker_id')
        Customer.objects.get(id=tasker_id).delete()
        return redirect(reverse('manager:verification_task'))


class DeleteTask(View):
    def post(self, request, **kwargs):
        task_model_id = kwargs.pop('task_model_id')
        TaskModel.objects.get(id=task_model_id).delete()
        return redirect(reverse('manager:task_model_list'))


class TaskerRegistration(FormView):
    template_name = 'manager/tasker_registration.html'
    form_class = TaskerRegistrationForm

    def form_valid(self, form):
        pass


# def tasker_registration(request):
#     if request.method == "POST":
#         additional_info_form = TaskerRegistrationForm(request.POST)
#         if additional_info_form.is_valid():
#             pass
#
#         else:
#             return render(request, 'additional-info.html', {'additional_info_form': additional_info_form})
#
#     else:
#         additional_info_form = TaskerRegistrationForm()
#         return render(request, 'additional-info.html',
#                       {'additional_info_form': additional_info_form})
